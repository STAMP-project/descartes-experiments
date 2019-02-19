import json
import jinja2
import os
import os.path
import argparse
from glob import glob
from collections import defaultdict
from itertools import count

MUTATION_STATUS = set([
    'KILLED', 
    'SURVIVED', 
    'TIMED_OUT', 
    'NON_VIABLE', 
    'MEMORY_ERROR', 
    'NOT_STARTED', 
    'STARTED', 
    'RUN_ERROR', 
    'NO_COVERAGE'
])

DETECTED_MUTATION_STATUS = set([
    'KILLED', 
    'TIMED_OUT', 
    'NON_VIABLE', 
    'MEMORY_ERROR', 
    'RUN_ERROR', 
])

REPORT_TEMPLATE = '''
# Mutation information

**Package:** {{ mutation.method_package | code }}

**Class:** {{ mutation.method_class | code }}

**Method:** {{ mutation.method_name | code }}

**Description:** {{ mutation.method_description | code }}

**Mutator:** {{ mutation.mutator | code }}

# Evolution

| Status | Detected | Test |
|--------|----------|------|
{% for res in results %}| {{ res.status | code }} | {{ res.is_detected | code }} | {{ res.detected_by | code }} |
{% endfor %}

# Covering tests

{% for test in mutation.covering_tests %}
* {{ test | code }}{% endfor %}
'''

INDEX_TEMPLATE = '''

# Unstable mutations

{% for mutation in mutations %}
* {{ mutation.mutator | code }} on {{ mutation.method | code }} [Details]({{ loop.index }}.md) {% endfor %}

# Covering tests

{% for test in tests %}
* {{ test | code }} {% endfor %}

'''

class Mutation:

    def __init__(self, json_record):
        self.mutator = json_record['mutator']
        
        method_record = json_record['method']
        self.method_name = method_record['name']
        self.method_description = method_record['description']
        self.method_class = method_record['class']
        self.method_package = method_record['package']
        
        self.covering_tests = json_record['tests']['ordered']
    
    @property
    def id(self):
        return f'{self.method}-{self.mutator}'
    
    @property
    def method(self):
        return f'{self.method_package}.{self.method_class}.{self.method_name}{self.method_description}'

    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)
    

class MutationResult:

    def __init__(self, json_record):
        self.status = json_record['status']
        self.detected_by = json_record['tests']['killer']
        self.executed = json_record['tests']['run']
    
    @property
    def is_detected(self):
        # Although the report already tells whether the mutation was detected
        # we follow the declared PIT convention
        return self.status in DETECTED_MUTATION_STATUS
    

def mutations_from_file(path):
    with open(path) as _file:
        document = json.load(_file)
        for record in document['mutations']:
            yield Mutation(record), MutationResult(record)

def get_mutation_evolution(files):
    evolution = defaultdict(lambda : [])

    for path in files:
        for mutation, result in mutations_from_file(path):
            evolution[mutation].append(result)
    
    return evolution

def detect_unstable_mutations(evolution):
    result = []

    for mutation, results in evolution.items():
        different_status = set(res.status for res in results)
        if len(different_status) > 1:
            result.append((mutation, results))
    
    return result

def generate_reports(mutations, destination):
    env = jinja2.Environment()
    env.filters['code'] = lambda x : f'`{x}`'

    index_template = env.from_string(INDEX_TEMPLATE)

    mutation_data = [m[0] for m in mutations]

    involved_tests = set()
    for mutation_record in mutation_data:
        involved_tests.update(mutation_record.covering_tests)

    with open(os.path.join(destination, 'index.md'), 'w') as index_file:
        index_template.stream(mutations=mutation_data, tests=involved_tests).dump(index_file)

    mutation_template = env.from_string(REPORT_TEMPLATE)
    for index, (mut, results) in zip(count(start=1), mutations):
        with open(os.path.join(destination, f'{index}.md'), 'w') as _file:
            mutation_template.stream(mutation=mut, results=results).dump(_file)

    

def readable_existing_directory(value):
    if os.path.isdir(value) and os.access(value, os.R_OK):
        return value
    raise ValueError("Reports should be stored in a readable folder")

def writable_directory(value):
    os.makedirs(value, exist_ok=True)
    return value

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--reports', default='target/pit-reports/', type=readable_existing_directory,
    help='Directory containig all mutation reports. By default they are located in target/pit-reports/')
    parser.add_argument('--output', default='unstable-mutations', type=writable_directory, help='Directory to store a report file for each unstable mutation found')
    return parser.parse_args()

def clear_directory(directory):
    for path in glob(os.path.join(directory, '*.md')):
        os.remove(path)

def main():
    arguments = parse_arguments()
    evolution = get_mutation_evolution(glob(os.path.join(arguments.reports, '*', 'mutations.json')))
    unstable_mutations = detect_unstable_mutations(evolution)
    clear_directory(arguments.output)
    generate_reports(unstable_mutations, arguments.output)


if __name__ == "__main__":
    main()

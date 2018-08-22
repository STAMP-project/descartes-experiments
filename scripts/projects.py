
import json
import os.path
from glob import glob


DEFAULT_BASE_FOLDER = os.path.abspath('../data')
STOP_METHOD_CATEGORIES = set([ 'EMPTY', 'ABSTRACT', 'HASH_CODE', 'SYNTHETIC', 'DEPRECATED', 'ENUM_METHOD', 'CONSTRUCTOR', 'SIMPLE_SETTER', 'SIMPLE_GETTER',  'RETURNS_CONSTANT', 'STATIC_INITIALIZER'])

def json_load(path):
    with open(path) as _file:
        return json.load(_file)

def method_id(record):
    package = record['package'].replace('/', '.')
    if not package.endswith('.'):
        package += '.'
    return package + '{class}.{name}{description}'.format(**record)

def is_stop_method(method):
    return not STOP_METHOD_CATEGORIES.isdisjoint(method['classifications'])

def is_written_method(method):
    classifications = set(method['classifications'])
    return classifications.isdisjoint(['SYNTHETIC', 'ABSTRACT', 'ENUM_METHOD']) and not (classifications.issuperset(['CONSTRUCTOR', 'DELEGATION']) and method['description'] == 'V()')

class Project:

    @staticmethod
    def available_projects(folder=DEFAULT_BASE_FOLDER):
        return map(Project, json_load(f'{folder}/projects.json'))

    def __init__(self, information, base_folder=DEFAULT_BASE_FOLDER):
        
        for attr, value in information.items():
            self.__setattr__(attr, value)

        self.base_folder = base_folder
        self.methods = json_load(f'{self.base_folder}/{self.id}/methods.json')
        self.stop_methods = [method for method in self.methods if is_stop_method(method)]
        self.target_methods = [method for method in self.methods if not is_stop_method(method)]
        self.written_methods = [method for method in self.methods if is_written_method(method)]

        self._stop_method_set = set(method_id(method) for method in self.stop_methods)

    def _load_report(self, name):
        return MutationReport.from_file(f'{self.base_folder}/{self.id}/{name}.json', self._stop_method_set)

    @property
    def descartes(self):
        return self._load_report('descartes')
    
    @property
    def gregor(self):
        return self._load_report('gregor')

class MutationReport:

    @staticmethod
    def from_file(path, stop_methods=set()):
        return MutationReport(json_load(path), stop_methods)
    
    def __init__(self, data, stop_methods=set()):
        self.data = data
        self.stop_methods = stop_methods
    
    @property
    def time(self):
        return self.data['time']

    @property
    def mutants(self):
        return map(Mutant, self.data['mutations'])

    @property    
    def meaningful_mutants(self):
        return [m for m in self.mutants if m.is_meaningful and m.method not in self.stop_methods]
    
    @property
    def covered_mutants(self):
        return [m for m in self.mutants if m.is_covered]


    @property
    def tests_by_method(self):
        result = {}
        for mutant in self.mutants:
            method = mutant.method
            tests = set(mutant.covering_tests)
            result[method] = result[method].union(tests) if method in result else tests
        return result
    
class Mutant:

    def __init__(self, data):
        self.data = data

    @property
    def killer_test(self):
        tests = self.data['tests']
        if 'killer'in tests:
            killer = self.data['tests']['killer']
            return killer if killer else None
        failing = tests['failing']
        return failing[0] if failing else None

    @property
    def method(self):
        return method_id(self.data['method'])

    @property
    def covering_tests(self):
        return self.data['tests']['ordered']

    @property
    def tests_run(self):
        return self.data['tests']['run']

    @property
    def detected(self):
        return self.data['detected']

    @property
    def is_meaningful(self):
        return self.is_covered and not self.is_trivial

    @property
    def is_covered(self):
        return self.data['status'] != 'NO_COVERAGE'
    
    @property
    def is_timed_out(self):
        return self.data['status'] == 'TIMED_OUT'

    @property
    def is_trivial(self):
        return self.detected and not self.killer_test

    @staticmethod
    def score(mutants):
        if not mutants:
            return -1
        count = 0
        for mut in mutants:
            if mut.detected:
                count += 1
        return count / len(mutants)

class MutantSet:

    def __init__(self):
        self.mutants = set()

    def add(self, mutant):
        self.mutants.add(mutant)
    
    @property
    def score(self):
        return Mutant.score(self.mutants)
    
    @property
    def tests(self):
        result = set()
        for mut in self.mutants:
            result.update(mut.covering_tests)
        return result

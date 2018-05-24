
import json
import os.path
from glob import glob


DEFAULT_BASE_FOLDER = os.path.abspath('../data')
STOP_METHOD_CATEGORIES = set([ 'EMPTY', 'ABSTRACT', 'HASH_CODE', 'SYNTHETIC', 'DEPRECATED', 'ENUM_METHOD', 'CONSTRUCTOR', 'SIMPLE_SETTER', 'SIMPLE_GETTER',  'RETURNS_CONSTANT' ])

def json_load(path):
    with open(path) as _file:
        return json.load(_file)

def method_id(record):
    record['package'] = record['package'].replace('/', '.')
    return '{package}{class}.{name}{description}'.format(**record) 

class Project:

    @staticmethod
    def available_projects(folder=DEFAULT_BASE_FOLDER):
        return json_load(f'{DEFAULT_BASE_FOLDER}/projects.json').map(Project)

    def __init__(self, information, base_folder=DEFAULT_BASE_FOLDER):
        
        for attr, value in information.items():
            self.__setattr__(attr, value)

        self.base_folder = base_folder
        self.stop_methods = self._load_stop_methods
    
    def _load_stop_methods(self):
        data = json_load(f'{self.base_folder}/methods.json')
        return set(method_id(item) for item in data if not STOP_METHOD_CATEGORIES.isdisjoint(item['classifications']))
    
    def _load_report(self, name):
        return MutationReport.from_file(json_load(f'{self.base_folder}/{self.id}/{name}.json'), self.stop_methods)

    @property
    def descartes(self):
        return self._load_report('descartes')
    
    @property
    def gregor(self):
        return self._load_report('gregor')

class MutationReport:

    @staticmethod
    def from_file(path, stop_methods=set()):
        with open(path) as _file:
            return MutationReport(json.load(_file), stop_methods)
    
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
        return self.data['tests']['killer']

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

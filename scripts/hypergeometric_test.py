from projects import Project
from scipy.stats import hypergeom
from pseudo_tested_methods import Record
from tables import ConsoleTableBuilder

def count_detected_mutants(mutants):
    return sum(m.detected for m in mutants)

def stats(project):
    record = Record(project)
    mutants_in_pseudo = [m for m in record.greg_mutants if m.method in record.pseudo_tested]
    return count_detected_mutants(mutants_in_pseudo), len(mutants_in_pseudo), count_detected_mutants(record.greg_mutants), len(record.greg_mutants)

def do_test(project):
    kps, ps, killed, total = stats(project)
    return hypergeom.cdf(kps, total, killed, ps)

def show_probabilities(projects, build_table=ConsoleTableBuilder):
    table = build_table(('Project',), ('Probability',))
    for proj in projects:
        table.row(proj.name, do_test(proj))
    table.display()

def main():
    show_probabilities(Project.available_projects())

if __name__ == '__main__':
    main()
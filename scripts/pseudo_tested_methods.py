from projects import Project, method_id, Mutant
from tables import ConsoleTableBuilder
import matplotlib.pyplot as plt

def percentage(x):
    return f'{100*x:.0f}%'

class Record:
    def __init__(self, project):
        self.id = project.id
        self.project = project
        self.methods = set(method_id(method) for method in project.written_methods)
        #Non-stop methods
        target_methods = set(method_id(method) for method in project.target_methods)
        descartes = project.descartes
        self.mutants = descartes.meaningful_mutants
        covered_methods = set(mut.method for mut in self.mutants)
        self.methods_under_analysis = covered_methods.intersection(target_methods)
        self.pseudo_tested = set(self.methods_under_analysis)
        for mut in self.mutants:
            if mut.detected:
                self.pseudo_tested.discard(mut.method)
        
        self.pt_ratio = len(self.pseudo_tested) / len(self.methods_under_analysis)

    @property
    def category_scores(self):
        mutants = self.project.gregor.meaningful_mutants
        pt = [mut for mut in mutants if mut.method in self.pseudo_tested]
        req = [mut for mut in mutants if mut.method not in self.pseudo_tested]
        values = (Mutant.score(pt), Mutant.score(req))
        return values

def show_rate_tables(records, build_table=ConsoleTableBuilder):
    table = build_table(('Project',), ('Methods', 'r'), ('Under Analysis', 'r'), ('Pseudo-tested', 'r'), ('Ratio', 'r', percentage))
    for item in records:
        table.row(item.id, len(item.methods), len(item.methods_under_analysis), len(item.pseudo_tested), item.pt_ratio)
    table.display()

def method_category_score(records):
    scores = [record.category_scores for record in records]
    xticks = range(len(records))
    yticks = [i/10 for i in range(11)]
    plt.figure(figsize=(5, 6))
    plt.yticks(yticks, map(percentage, yticks))
    plt.xticks(xticks, [r.project.name for r in records], rotation='vertical')
    plt.scatter(xticks, [s[0] for s in scores])
    plt.scatter(xticks, [s[1] for s in scores])
    plt.legend(['Required', 'Pseudo-tested'])
    plt.tight_layout()
    plt.show()

def main():
    records = [Record(project) for project in Project.available_projects()]
    show_rate_tables(records)
    method_category_score(records)

if __name__ == "__main__":
    main()
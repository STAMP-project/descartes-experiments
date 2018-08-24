from projects import Project, method_id, Mutant
from tables import ConsoleTableBuilder, percentage
import matplotlib.pyplot as plt
from itertools import chain, cycle
from collections import defaultdict



class Record:
    def __init__(self, project):
        self.id = project.id
        self.project = project
        self.methods = set(method_id(method) for method in project.written_methods)
        #Non-stop methods
        target_methods = set(method_id(method) for method in project.target_methods)
        descartes = project.descartes
        
        self.desc_mutants = descartes.meaningful_mutants
        covered_methods = set(mut.method for mut in self.desc_mutants)
        self.methods_under_analysis = covered_methods.intersection(target_methods)
        self.pseudo_tested = set(self.methods_under_analysis)
        for mut in self.desc_mutants:
            if mut.detected:
                self.pseudo_tested.discard(mut.method)
        
        self.greg_mutants = project.gregor.meaningful_mutants
        self.pt_ratio = len(self.pseudo_tested) / len(self.methods_under_analysis)

    @property
    def category_scores(self):
        pt = [mut for mut in self.greg_mutants if mut.method in self.pseudo_tested]
        req = [mut for mut in self.greg_mutants if mut.method not in self.pseudo_tested]
        values = (Mutant.score(pt), Mutant.score(req))
        return values
    
    def _get_method_scores(self, methods):
        grouped_mutants = defaultdict(lambda: [])
        for mutant in self.greg_mutants:
            method = mutant.method
            if method not in methods:
                continue
            grouped_mutants[method].append(mutant)
        return [Mutant.score(grp) for grp in grouped_mutants.values() if len(grp) > 0]

    @property
    def score_distributions(self):
        return \
            self._get_method_scores(self.pseudo_tested), \
            self._get_method_scores(self.methods_under_analysis.difference(self.pseudo_tested))
        

def show_rates_table(records, build_table=ConsoleTableBuilder):
    table = build_table(('Project',), ('Methods', 'r'), ('Under Analysis', 'r'), ('Pseudo-tested', 'r'), ('Ratio', 'r', percentage))
    for item in records:
        table.row(item.project.name, len(item.methods), len(item.methods_under_analysis), len(item.pseudo_tested), item.pt_ratio)
    table.display()

def method_category_score(records):
    scores = [record.category_scores for record in records]
    xticks = range(len(records))
    yticks = [i/10 for i in range(11)]
    plt.figure(figsize=(6, 6))
    plt.yticks(yticks, map(percentage, yticks))
    plt.xticks(xticks, [r.project.name for r in records], rotation='vertical')
    plt.scatter(xticks, [s[0] for s in scores])
    plt.scatter(xticks, [s[1] for s in scores])
    plt.legend(['Pseudo-tested', 'Required'])
    plt.tight_layout()

def chained_list(elements):
    return list(chain(*elements))

def method_score_distributions(records):
    plt.figure(figsize=(6,8))
    distributions = chained_list(rec.score_distributions for rec in records)
    positions = chained_list([4*i+1, 4*i+2] for i in range(len(records)))
    plt.yticks([1.5 + i*4 for i in range(len(records))], [r.project.name for r in records])
    xticks = [i/5 for i in range(6)]
    plt.xticks(xticks, map(percentage, xticks))
    parts = plt.violinplot(distributions, vert=False, showextrema=False, points=10, widths=1, showmeans=True, positions=positions)
    for pc, color in zip(parts['bodies'], cycle(['C0', 'C1'])):
        pc.set_facecolor(color)
        pc.set_alpha(1)
    plt.tight_layout()
    plt.legend(['Pseudo-tested', 'Required'])

    
    

def main():
    print("Loading data. This may take some time.")
    records = [Record(project) for project in Project.available_projects()]
    show_rates_table(records)
    method_category_score(records)
    method_score_distributions(records)
    plt.show()

if __name__ == "__main__":
    main()
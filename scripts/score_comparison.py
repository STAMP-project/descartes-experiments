
from table_printer import table
from projects import Project, Mutant
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from tables import ConsoleTableBuilder

class ScoreRecord:
    def __init__(self, mutants):
        self.total = len(mutants)
        self.killed = len([m for m in mutants if m.detected])
        self.score = self.killed / self.total

def methods_in_common(mutants, others):
    methods = set(m.method for m in mutants)
    other_methods = set(m.method for m in others)
    return methods.intersection(other_methods)

def get_score_record(mutants, methods):
    return ScoreRecord([m for m in mutants if m.method in methods])

def get_both_scores(project):
    descartes = project.descartes.covered_mutants
    gregor = project.gregor.covered_mutants
    methods = methods_in_common(descartes, gregor)
    return (get_score_record(descartes, methods), get_score_record(gregor, methods))

def render_table(names, scores, build_table=ConsoleTableBuilder):
    percentage = lambda x: f'{100*x:.2f}'
    table = build_table(
        ('Project',), 
        ('Mutants', 'r'), 
        ('Killed' , 'r'), 
        ('Score'  , 'r', percentage), 
        ('Mutants', 'r'), 
        ('Killed' , 'r'), 
        ('Score'  , 'r', percentage))
    for name, (descartes, gregor) in zip(names, scores) :
        table.row(name, descartes.total, descartes.killed, descartes.score, gregor.total, gregor.killed, gregor.score)
    table.display()

def show_plot(descartes, gregor):
    plt.xlim(50, 100)
    plt.ylim(50, 100)
    plt.scatter([100*i for i in descartes], [100*j for j in gregor])
    plt.xlabel('Descartes')
    plt.ylabel('Gregor')
    plt.show()

def main():
    projects = list(Project.available_projects())
    #Compute the scores
    print('Computing the scores. This may take a while...')
    scores = [get_both_scores(p) for p in projects]
    descartes_scores = [c[0].score for c in scores]
    gregor_scores = [c[1].score for c in scores]
    #Show the table
    render_table([p.name for p in projects], scores)
    #Show the correlation
    correlation = spearmanr(descartes_scores, gregor_scores)
    print(f'The Spearman correlation coefficient is {correlation.correlation} with a p-value of {correlation.pvalue}')
    #Show plot
    show_plot(descartes_scores, gregor_scores)

if __name__ == '__main__':
    main()
    
    



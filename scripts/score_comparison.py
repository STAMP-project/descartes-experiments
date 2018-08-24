from projects import Project, Mutant
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.stats import spearmanr
from tables import ConsoleTableBuilder, percentage
import numpy as np

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
    plt.scatter(descartes, gregor)

    ticks = np.linspace(.5, 1, 6)
    lables = [percentage(t) for t in ticks]
    plt.xticks(ticks, lables)
    plt.yticks(ticks, lables)

    plt.xlabel('Descartes')
    plt.ylabel('Gregor')

def bland_altman_plot(descartes, gregor):
    x = np.add(descartes, gregor)/2
    y = np.subtract(descartes, gregor)

    mean = np.mean(y)
    stdv = np.std(y)
    plt.figure()
    plt.ylim(mean-3*stdv, mean + 3*stdv)
    plt.xlabel("(Descartes-Gregor)/2")
    plt.ylabel("Descartes - Gregor")
    plt.scatter(x, y)

    ax = plt.gca()
    xmin, xmax = ax.get_xbound()
    color = 'red'

    #Lines
    lower = mean - 2*stdv
    upper = mean + 2*stdv
    ax.add_line(Line2D([xmin, xmax], [mean, mean], color=color))
    ax.add_line(Line2D([xmin, xmax], [lower, lower], color=color, linestyle='--'))
    ax.add_line(Line2D([xmin, xmax], [upper, upper], color=color, linestyle='--'))




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
    bland_altman_plot(descartes_scores, gregor_scores)
    plt.show()

if __name__ == '__main__':
    main()
    
    



from tables import ConsoleTableBuilder
from projects import Project
import matplotlib.pyplot as plt


def time_format(time):
    time, milliseconds = divmod(time, 1000)
    time, seconds = divmod(time, 60)
    time, minutes = divmod(time, 60)
    return '{}:{:02}:{:02}'.format(time, minutes, seconds)

def time_table(projects, build_table=ConsoleTableBuilder):
    table = build_table(('Project',), ('Descartes', 'r', time_format), ('Gregor', 'r', time_format))
    for name, descartes, gregor in projects:
        table.row(name, descartes.time, gregor.time)
    table.display()

def mutants_table(projects, build_table=ConsoleTableBuilder):
    table = build_table(('Project',), ('Descartes', 'r'), ('Gregor', 'r'))
    for name, descartes, gregor in projects:
        table.row(name, descartes.mutants, gregor.mutants)
    table.display()

def gain_plot(dvalues, gvalues, names, format=str):
    ratios = [dv/dg for dv,dg in zip(dvalues, gvalues)]
    plt.figure(figsize=(12,6))
    ax = plt.subplot(111)
    width = .6
    offset = .35
    positions = [2*i for i in range(len(ratios))]

    dbars = plt.bar([pos - offset for pos in positions], ratios, width=width)
    for value, bar in zip(dvalues, dbars):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, format(value), rotation='vertical', ha='center', va='bottom')

    gbars = plt.bar([pos + offset for pos in positions], [1 for i in range(len(ratios))], width=width)
    for value, bar in zip(gvalues, gbars):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.01, format(value), rotation='vertical', ha='center', va='top', color='white')
    
    plt.xticks(positions, names, rotation='vertical')
    yticks = [i/10 for i in range(11)]
    plt.yticks(yticks, [f'{100*y:.0f}%' for y in yticks])
    plt.legend(['Descartes', 'Gregor'], ncol=2, loc='upper center', bbox_to_anchor=(.5, 1.06), framealpha=1, edgecolor='black') 
    
    plt.tight_layout()

def plot_times(projects):
    gain_plot(
        [p[1].time for p in projects], 
        [p[2].time for p in projects],
        [p[0] for p in projects],
        time_format)

def plot_mutants(projects):
    gain_plot(
        [p[1].mutants for p in projects], 
        [p[2].mutants for p in projects],
        [p[0] for p in projects])

class Record:
    def __init__(self, report):
        self.time = report.time
        self.mutants = len(list(report.mutants))

def main():
    print('Loading data. This may take a while...')
    projects = [(p.name, Record(p.descartes), Record(p.gregor)) for p in Project.available_projects()]
    print('Execution time:')
    time_table(projects)
    plot_times(projects)
    print('Number of mutants created:')
    mutants_table(projects)
    plot_mutants(projects)
    plt.show()


if __name__ == '__main__':
    main()




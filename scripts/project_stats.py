from tables import ConsoleTableBuilder
from projects import Project


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
        table.row(name, len(list(descartes.mutants)), len(list(gregor.mutants)))
    table.display()


def main():
    print('Loading data. This may take a while...')
    projects = [(p.name, p.descartes, p.gregor) for p in Project.available_projects()]
    print('Execution time:')
    time_table(projects)
    print('Number of mutants created:')
    mutants_table(projects)


if __name__ == '__main__':
    main()




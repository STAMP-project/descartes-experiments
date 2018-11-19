from tables import ConsoleTableBuilder
from projects import Project, method_id
from pseudo_tested_methods import Record
import matplotlib.pyplot as plt


def get_data():
    for project in Project.available_projects():
        record = Record(project)
        non_accessible_methods = set(method_id(m) for m in project.methods if 'ACCESSIBLE' not in m['classifications'])
        all_methods = set(method_id(m) for m in project.methods)
        def ratio(a_set):
            return len(a_set.intersection(non_accessible_methods))/len(a_set)
        yield (project.name, ratio(record.pseudo_tested), ratio(record.methods_under_analysis), ratio(all_methods))

def table(data, build_table=ConsoleTableBuilder):
    table = build_table( ('Project', ), ('Pseudo-tested', 'r'), ('Under analysis', 'r'), ('All methods', 'r'))
    for name, ptr, uar, amr in data:
        table.row(name, ptr, uar, amr)
    table.display()

def plot(data):
    ptr = [tup[1] for tup in data]
    uar = [tup[2] for tup in data]
    amr = [tup[3] for tup in data]
    labels = [tup[0] for tup in data]
    positions = [i for i in range(len(labels))]
    width = 0.3
    plt.figure(figsize=(12, 6))
    plt.bar([i for i in range(len(labels))], ptr, width=width, color='orange')
    plt.bar([i-width for i in range(len(labels))], uar, width=width, color='green')
    plt.bar([i+width for i in range(len(labels))], amr, width=width, color='blue')
    plt.xticks(positions, labels, rotation='vertical')
    plt.legend(['Pseudo-tested', 'Under analysis', 'All'])
    plt.tight_layout()

    

def main():
    data = list(get_data())
    table(data)
    plot(data)
    plt.show()
    

    
if __name__ == '__main__':
    main()
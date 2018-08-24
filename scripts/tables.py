from itertools import count, zip_longest
from collections import namedtuple
from IPython.display import HTML, display

CONSOLE_ALIGNMENTS = {'l': str.ljust, 'r': str.rjust, 'c': str.center}

ALIGNMENTS = set(['l', 'r', 'c'])

def percentage(x):
    '''
    Percentage string format
    '''
    return f'{100*x:.0f}%'

class Column:
    def __init__(self, title, alignment='l', given_format='{}'):
        self.title = str(title)
        
        if type(alignment) is not str or not alignment or alignment[0] not in ALIGNMENTS:
            raise Exception(f'Incorrect alignment «{alignment}». Value must be a string begining with: ' + ','.join(ALIGNMENTS))

        self.alignment = {'l':'left', 'r':'right', 'c':'center'}[alignment[0]]

        if type(given_format) is str:
            self.format = lambda x: given_format.format(x)
        elif callable(given_format):
            self.format = given_format
        else:
            raise Exception(f'Incorrect column format «{given_format}» for column. Value must be a string or a callable.')

class ConsoleColumn(Column):
    def __init__(self, *args, **kwargs):
        super(ConsoleColumn, self).__init__(*args, **kwargs)
        self.width = len(self.title)
        self.alignment = {'left': str.ljust, 'right': str.rjust, 'center': str.center}[self.alignment]

    def align(self, value):
        return self.alignment(value, self.width)
    
    def display(self, value):
        return self.align(self.format(value))

class ConsoleTableBuilder:
    
    def __init__(self, *definitions):
        self.column_definitions = self._get_column_definitions(list(definitions))
        self.rows = []
    
    def _get_column_definitions(self, definitions):
        for i, d in zip(count(), definitions):
            if type(d) is not tuple or not d or len(d) > 3:
                raise Exception(f'Invalid column definition «{d}» for column {i}. All column definitions must be tuples with at least one element and no more than three.')
        return [ ConsoleColumn(*column) for column in definitions]

    def row(self, *values):
        row = list(values)
        pairs = zip(self.column_definitions, row) if len(row) > len(self.column_definitions) else zip_longest(self.column_definitions, row, fillvalue='')
        new_row = []
        for column, value in pairs:
            actual_value = column.format(value)
            column.width = max(len(actual_value), column.width)
            new_row.append(actual_value)
        self.rows.append(new_row)
        return self

    def _display_row(self, row):
        print('| {} |'.format( ' | '.join( column.align(value) for column, value in zip(self.column_definitions, row))    ))
    
    def _display_headers(self):
        self._display_row(column.title for column in self.column_definitions)
        print('|{}|'.format('|'.join('-'*(column.width + 2) for column in self.column_definitions)))

    def display(self):
        self._display_headers()
        for row in self.rows:
            self._display_row(row)

class IPythonColumn(Column):
    def __init__(self, *args, **kwargs):
        super(IPythonColumn, self).__init__(*args, **kwargs)
    
    def cell(self, value):

        return f'<td>{self.format(value)}</td>'
    
    def header(self):
        style = f' style="text-align:{self.alignment}"' if self.alignment != 'left' else ''
        return f'<th{style}>{self.title}</th>'

class IPythonTableBuilder:

    def __init__(self, *definitions):
        self.columns = [IPythonColumn(*col) for col in definitions]
        self.content = '<tr>{}</tr>'.format( ''.join(col.header() for col in self.columns))
    
    def row(self, *values):
        self.content += '<tr>{}</tr>'.format( ''.join(col.cell(val) for col, val in zip(self.columns, values)))
    
    def display(self):
        display(HTML(f'<table>{self.content}</table>'))

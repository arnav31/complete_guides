import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    "id": [1,2,3,4],
    "name": ["alice","bob","charlie","dave"],
    "age": [25, 30, np.nan, 40],
    "score": [85, 92, 78, 90],
    "joined": ["2020-01-05","2021-06-10","2022-03-15","2020-12-01"]
})

print("=" * 80)
print("METHOD 1: Standard pandas with better config")
print("=" * 80)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.colheader_justify', 'center')
print(df)

print("\n" + "=" * 80)
print("METHOD 2: Using tabulate library (pip install tabulate)")
print("=" * 80)
try:
    from tabulate import tabulate
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    print("\nOther tablefmt options: 'fancy_grid', 'pretty', 'psql', 'github', 'html'")
except ImportError:
    print("Install tabulate: pip install tabulate")

print("\n" + "=" * 80)
print("METHOD 3: Using rich library (pip install rich)")
print("=" * 80)
try:
    from rich.console import Console
    from rich.table import Table
    
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    
    # Add columns
    for col in df.columns:
        table.add_column(col)
    
    # Add rows
    for idx, row in df.iterrows():
        table.add_row(*[str(val) for val in row])
    
    console.print(table)
except ImportError:
    print("Install rich: pip install rich")

print("\n" + "=" * 80)
print("METHOD 4: DataFrame to_string with formatting")
print("=" * 80)
print(df.to_string(index=False, max_colwidth=20, justify='center'))

print("\n" + "=" * 80)
print("METHOD 5: Using df.to_markdown (pip install tabulate)")
print("=" * 80)
try:
    print(df.to_markdown(index=False))
except ImportError:
    print("Install tabulate for markdown: pip install tabulate")

print("\n" + "=" * 80)
print("METHOD 6: Styled DataFrame (works in Jupyter/HTML)")
print("=" * 80)
styled = df.style\
    .highlight_max(axis=0, color='lightgreen')\
    .highlight_min(axis=0, color='lightcoral')\
    .format(precision=2)
print("Use styled.to_html() for HTML output or display in Jupyter")

# If you want color in terminal
print("\n" + "=" * 80)
print("METHOD 7: Using prettytable (pip install prettytable)")
print("=" * 80)
try:
    from prettytable import PrettyTable
    pt = PrettyTable()
    pt.field_names = df.columns.tolist()
    for row in df.itertuples(index=False):
        pt.add_row(row)
    print(pt)
except ImportError:
    print("Install prettytable: pip install prettytable")


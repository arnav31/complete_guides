import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table
from rich import box

# Initialize Rich console
console = Console()

# small sample DataFrame used in many examples
df = pd.DataFrame({
    "id": [1,2,3,4],
    "name": ["alice","bob","charlie","dave"],
    "age": [25, 30, np.nan, 40],
    "score": [85, 92, 78, 90],
    "joined": ["2020-01-05","2021-06-10","2022-03-15","2020-12-01"]
})

# Function to convert DataFrame to Rich Table
def df_to_rich_table(df, title="DataFrame", show_index=False):
    """Convert pandas DataFrame to rich Table"""
    table = Table(title=title, box=box.ROUNDED, show_header=True, header_style="bold cyan")
    
    # Add index column if requested
    if show_index:
        table.add_column("Index", style="dim")
    
    # Add columns
    for col in df.columns:
        table.add_column(str(col), style="magenta")
    
    # Add rows
    for idx, row in df.iterrows():
        row_data = [str(val) for val in row]
        if show_index:
            row_data = [str(idx)] + row_data
        table.add_row(*row_data)
    
    return table

# Save and load CSV/Excel
df.to_csv("data.csv")
df = pd.read_csv("data.csv")         # load CSV
df.to_csv("out.csv", index=False)   # save CSV
df.to_excel("out.xlsx", index=False)

# Display with Rich
console.print("\n[bold green]📊 HEAD (first 5 rows)[/bold green]")
console.print(df_to_rich_table(df.head(), "df.head()"))

console.print("\n[bold yellow]📊 TAIL (last 2 rows)[/bold yellow]")
console.print(df_to_rich_table(df.tail(2), "df.tail(2)"))

console.print("\n[bold blue]ℹ️  INFO[/bold blue]")
console.print(df.info())

console.print("\n[bold magenta]📈 DESCRIBE (numeric summary)[/bold magenta]")
console.print(df_to_rich_table(df.describe(), "df.describe()", show_index=True))

console.print(f"\n[bold cyan]📐 SHAPE:[/bold cyan] {df.shape} (rows, cols)")

console.print("\n[bold red]📋 DTYPES[/bold red]")
for col, dtype in df.dtypes.items():
    console.print(f"  • {col}: [yellow]{dtype}[/yellow]")

console.print("\n[bold green]🔢 VALUE COUNTS (name column)[/bold green]")
value_counts_df = df['name'].value_counts().reset_index()
value_counts_df.columns = ['name', 'count']
console.print(df_to_rich_table(value_counts_df, "df['name'].value_counts()"))


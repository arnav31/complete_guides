import pandas as pd
import numpy as np
from rich.console import Console
from rich import box
from rich.table import Table

# Initialize Rich console for beautiful output
console = Console()

# Configure pandas display options for prettier output
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Auto-detect terminal width
pd.set_option('display.max_colwidth', 50)   # Max column width
pd.set_option('display.precision', 2)       # Decimal precision
pd.set_option('display.colheader_justify', 'center')  # Center column headers

# Helper function to convert DataFrame to Rich Table
def df_to_table(df, title=""):
    """Convert pandas DataFrame to Rich Table for beautiful display"""
    table = Table(title=title, box=box.ROUNDED, show_header=True, header_style="bold cyan")
    
    # Add columns
    for col in df.columns:
        table.add_column(str(col), style="magenta")
    
    # Add rows (limit to 10 for display)
    for idx, row in df.head(10).iterrows():
        table.add_row(*[str(val) for val in row])
    
    return table

# small sample DataFrame used in many examples
df = pd.DataFrame({
    "id": [1,2,3,4],
    "name": ["alice","bob","charlie","dave"],
    "age": [25, 30, np.nan, 40],
    "score": [85, 92, 78, 90],
    "joined": ["2020-01-05","2021-06-10","2022-03-15","2020-12-01"]
})
df.to_csv("data.csv")
df = pd.read_csv("data.csv")         # load CSV
df.to_csv("out.csv", index=False)   # save CSV
df.to_excel("out.xlsx", index=False)
# df = pd.read_json("data.json")

# Display with beautiful Rich formatting
console.print("\n[bold green]📊 HEAD - First 5 rows[/bold green]")
console.print(df_to_table(df.head(), "df.head()"))

console.print("\n[bold yellow]📊 TAIL - Last 2 rows[/bold yellow]")
console.print(df_to_table(df.tail(2), "df.tail(2)"))

console.print("\n[bold blue]ℹ️  INFO - Schema & Types[/bold blue]")
df.info()

console.print("\n[bold magenta]📈 DESCRIBE - Statistical Summary[/bold magenta]")
console.print(df_to_table(df.describe(), "df.describe()"))

console.print(f"\n[bold cyan]📐 SHAPE:[/bold cyan] {df.shape} (rows, columns)")

console.print("\n[bold red]📋 DTYPES - Column Types[/bold red]")
for col, dtype in df.dtypes.items():
    console.print(f"  • {col}: [yellow]{dtype}[/yellow]")

console.print("\n[bold green]🔢 VALUE_COUNTS - Name column[/bold green]")
value_counts_df = df['name'].value_counts().reset_index()
value_counts_df.columns = ['name', 'count']
console.print(df_to_table(value_counts_df, "df['name'].value_counts()"))

console.print("\n[bold white]🎯 SELECTION EXAMPLES[/bold white]")
console.print(f"\n[cyan]df.loc[0, 'name']:[/cyan] {df.loc[0, 'name']}")
console.print("[dim]Description: Label-based single value selection[/dim]")

console.print("\n[cyan]df.iloc[1:3, 0:2] - Integer location slicing:[/cyan]")
console.print(df_to_table(df.iloc[1:3, 0:2], "df.iloc[1:3, 0:2]"))

console.print(f"\n[cyan]df.at[1, 'age']:[/cyan] {df.at[1, 'age']}")
console.print("[dim]Description: Fast scalar access (label-based)[/dim]")

console.print(f"\n[cyan]df.iat[2, 3]:[/cyan] {df.iat[2, 3]}")
console.print("[dim]Description: Fast scalar access (integer-based)[/dim]")

console.print("\n[cyan]df[df['age'] > 30] - Boolean filter:[/cyan]")
console.print(df_to_table(df[df["age"] > 30], "df[df['age'] > 30]"))

console.print("\n[cyan]df.query('score >= 90') - Query method:[/cyan]")
console.print(df_to_table(df.query("score >= 90"), "df.query('score >= 90')"))
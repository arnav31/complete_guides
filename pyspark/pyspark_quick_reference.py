"""
PYSPARK QUICK REFERENCE CHEATSHEET
One-page summary of most important functions
"""

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

print("=" * 80)
print("PYSPARK QUICK REFERENCE - Most Important Functions")
print("=" * 80)

# Essential Functions Table
table = Table(title="Essential PySpark Functions", box=box.ROUNDED, show_header=True, header_style="bold cyan")
table.add_column("Category", style="yellow", width=20)
table.add_column("Function", style="magenta", width=35)
table.add_column("Description", style="green", width=20)

# DataFrame Creation
table.add_row("Creation", "spark.createDataFrame(data)", "Create from list/RDD")
table.add_row("", "spark.read.csv(path)", "Read CSV file")
table.add_row("", "spark.read.parquet(path)", "Read Parquet file")
table.add_row("", "spark.read.json(path)", "Read JSON file")

# Basic Operations
table.add_row("Selection", "df.select(cols)", "Select columns")
table.add_row("", "df.filter(condition)", "Filter rows")
table.add_row("", "df.where(condition)", "Same as filter")
table.add_row("", "df.limit(n)", "Limit to n rows")

# Transformations
table.add_row("Transform", "df.withColumn(name, col)", "Add/modify column")
table.add_row("", "df.withColumnRenamed(old, new)", "Rename column")
table.add_row("", "df.drop(cols)", "Drop columns")
table.add_row("", "df.dropDuplicates([cols])", "Remove duplicates")
table.add_row("", "df.orderBy(cols)", "Sort DataFrame")

# Aggregations
table.add_row("Aggregate", "df.count()", "Count rows")
table.add_row("", "df.groupBy(cols).agg()", "Group and aggregate")
table.add_row("", "df.agg(functions)", "Aggregate functions")

# Joins
table.add_row("Joins", "df1.join(df2, on, how)", "Join DataFrames")
table.add_row("", "df1.union(df2)", "Union (vertical stack)")
table.add_row("", "df1.unionByName(df2)", "Union by column name")

# Actions
table.add_row("Actions", "df.show(n)", "Display n rows")
table.add_row("", "df.collect()", "Return all rows")
table.add_row("", "df.take(n)", "Return first n rows")
table.add_row("", "df.first()", "Return first row")
table.add_row("", "df.count()", "Count rows")

# I/O Operations
table.add_row("I/O", "df.write.csv(path)", "Write to CSV")
table.add_row("", "df.write.parquet(path)", "Write to Parquet")
table.add_row("", "df.write.mode('overwrite')", "Overwrite mode")

# Performance
table.add_row("Performance", "df.cache() / persist()", "Cache DataFrame")
table.add_row("", "df.repartition(n)", "Change partitions")
table.add_row("", "df.coalesce(n)", "Reduce partitions")
table.add_row("", "broadcast(df)", "Broadcast join hint")

console.print(table)

# Column Functions
console.print("\n[bold]📊 COLUMN FUNCTIONS[/bold]")
console.print("=" * 80)

functions_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
functions_table.add_column("Category", style="yellow", width=20)
functions_table.add_column("Functions", style="magenta", width=55)

functions_table.add_row("String", "upper, lower, length, substring, concat, trim, ltrim, rtrim")
functions_table.add_row("", "split, regexp_replace, regexp_extract, concat_ws")
functions_table.add_row("Numeric", "abs, ceil, floor, round, sqrt, pow, exp, log")
functions_table.add_row("", "sin, cos, tan, rand, randn")
functions_table.add_row("Aggregate", "sum, avg, mean, min, max, count, countDistinct")
functions_table.add_row("", "first, last, stddev, variance, collect_list, collect_set")
functions_table.add_row("Date/Time", "current_date, current_timestamp, to_date, to_timestamp")
functions_table.add_row("", "year, month, dayofmonth, hour, minute, second")
functions_table.add_row("", "date_add, date_sub, datediff, date_format, unix_timestamp")
functions_table.add_row("Conditional", "when, otherwise, coalesce, isNull, isNotNull")
functions_table.add_row("", "isin, like, rlike, cast")
functions_table.add_row("Window", "row_number, rank, dense_rank, lag, lead")
functions_table.add_row("", "percent_rank, ntile, cume_dist")
functions_table.add_row("Array", "array, array_contains, explode, size, sort_array")
functions_table.add_row("Map", "map, map_keys, map_values, explode")

console.print(functions_table)

# SQL Operations
console.print("\n[bold]🗄️  SQL OPERATIONS[/bold]")
console.print("=" * 80)

sql_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
sql_table.add_column("Operation", style="magenta", width=40)
sql_table.add_column("Description", style="yellow", width=35)

sql_table.add_row("df.createOrReplaceTempView('table')", "Create temp view for SQL")
sql_table.add_row("spark.sql('SELECT * FROM table')", "Execute SQL query")
sql_table.add_row("df.registerTempTable('table')", "Register as temp table (deprecated)")

console.print(sql_table)

# Join Types
console.print("\n[bold]🔗 JOIN TYPES[/bold]")
console.print("=" * 80)

join_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
join_table.add_column("Join Type", style="magenta", width=20)
join_table.add_column("Description", style="yellow", width=55)

join_table.add_row("inner", "Returns matching rows from both DataFrames")
join_table.add_row("left / left_outer", "All rows from left, matching from right")
join_table.add_row("right / right_outer", "All rows from right, matching from left")
join_table.add_row("outer / full / full_outer", "All rows from both DataFrames")
join_table.add_row("left_semi", "Rows from left that have match in right (left columns only)")
join_table.add_row("left_anti", "Rows from left with NO match in right")
join_table.add_row("cross", "Cartesian product of both DataFrames")

console.print(join_table)

# Live Examples
console.print("\n[bold]💻 TOP 10 LIVE EXAMPLES[/bold]")
console.print("=" * 80)

examples = [
    ("1. Filter rows", "df.filter(col('age') > 30)"),
    ("2. Select columns", "df.select('name', 'age', 'department')"),
    ("3. Add column", "df.withColumn('bonus', col('salary') * 0.1)"),
    ("4. Group & aggregate", "df.groupBy('dept').agg(avg('salary'))"),
    ("5. Join DataFrames", "df1.join(df2, df1.id == df2.id, 'inner')"),
    ("6. Sort data", "df.orderBy(col('salary').desc())"),
    ("7. Handle nulls", "df.fillna({'age': 0, 'name': 'Unknown'})"),
    ("8. Window function", "row_number().over(Window.partitionBy('dept').orderBy('salary'))"),
    ("9. Conditional column", "when(col('age') > 30, 'Senior').otherwise('Junior')"),
    ("10. SQL query", "spark.sql('SELECT * FROM table WHERE age > 30')"),
]

for title, code in examples:
    console.print(f"[yellow]{title}[/yellow]")
    console.print(f"  [green]{code}[/green]")

# Schema Definition
console.print("\n[bold]📋 SCHEMA DEFINITION[/bold]")
console.print("=" * 80)

schema_example = """
from pyspark.sql.types import *

schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("name", StringType(), nullable=True),
    StructField("age", IntegerType(), nullable=True),
    StructField("salary", DoubleType(), nullable=True),
    StructField("date", DateType(), nullable=True)
])

df = spark.createDataFrame(data, schema)
"""
console.print(f"[green]{schema_example}[/green]")

# Common Data Types
console.print("\n[bold]🔤 COMMON DATA TYPES[/bold]")
console.print("=" * 80)

types_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
types_table.add_column("Type", style="magenta", width=25)
types_table.add_column("Description", style="yellow", width=50)

types_table.add_row("IntegerType()", "32-bit signed integer")
types_table.add_row("LongType()", "64-bit signed integer")
types_table.add_row("DoubleType()", "64-bit floating point")
types_table.add_row("FloatType()", "32-bit floating point")
types_table.add_row("StringType()", "String / character")
types_table.add_row("BooleanType()", "True or False")
types_table.add_row("DateType()", "Date (year-month-day)")
types_table.add_row("TimestampType()", "Date and time")
types_table.add_row("ArrayType(elementType)", "Array of elements")
types_table.add_row("MapType(keyType, valueType)", "Map of key-value pairs")
types_table.add_row("StructType([StructField...])", "Structured row")

console.print(types_table)

# Window Functions Example
console.print("\n[bold]🪟 WINDOW FUNCTIONS EXAMPLE[/bold]")
console.print("=" * 80)

window_example = """
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lag, lead

# Define window spec
window_spec = Window.partitionBy('department').orderBy(col('salary').desc())

df.withColumn('row_num', row_number().over(window_spec)) \\
  .withColumn('rank', rank().over(window_spec)) \\
  .withColumn('dense_rank', dense_rank().over(window_spec)) \\
  .withColumn('prev_salary', lag('salary', 1).over(window_spec)) \\
  .withColumn('next_salary', lead('salary', 1).over(window_spec))

# Running total
window_running = Window.partitionBy('dept').orderBy('id') \\
                      .rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn('running_total', sum('salary').over(window_running))
"""
console.print(f"[green]{window_example}[/green]")

# UDF Example
console.print("\n[bold]🔧 USER DEFINED FUNCTIONS (UDF)[/bold]")
console.print("=" * 80)

udf_example = """
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Regular UDF
def categorize(value):
    return "High" if value > 100 else "Low"

categorize_udf = udf(categorize, StringType())
df.withColumn('category', categorize_udf(col('amount')))

# Pandas UDF (Vectorized - More efficient)
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(StringType())
def categorize_pandas(value: pd.Series) -> pd.Series:
    return value.apply(lambda x: "High" if x > 100 else "Low")

df.withColumn('category', categorize_pandas(col('amount')))
"""
console.print(f"[green]{udf_example}[/green]")

# Interview Tips
console.print("\n[bold]💡 INTERVIEW TIPS[/bold]")
console.print("=" * 80)

tips = [
    "Transformations are lazy (not executed immediately)",
    "Actions trigger actual computation (show, collect, count)",
    "Use broadcast() for joining large table with small table",
    "cache() or persist() for DataFrames used multiple times",
    "Avoid collect() on large DataFrames (OOM risk)",
    "Use coalesce() instead of repartition() to reduce partitions",
    "Window functions don't need shuffle when PARTITION BY matches existing partitioning",
    "pandas_udf is much faster than regular udf (vectorized)",
    "Use explain() to view execution plan",
    "Parquet is usually better than CSV for storage",
]

for i, tip in enumerate(tips, 1):
    console.print(f"[cyan]{i:2}.[/cyan] {tip}")

# Common Mistakes
console.print("\n[bold]⚠️  COMMON MISTAKES[/bold]")
console.print("=" * 80)

mistakes = [
    ("Using collect() on large data", "Use take(), show(), or write to storage"),
    ("Not caching reused DataFrames", "Use cache() for DataFrames used multiple times"),
    ("Using UDF instead of built-in", "Built-in functions are optimized, use them first"),
    ("Wrong number of partitions", "Too few: underutilize cluster. Too many: overhead"),
    ("Forgetting to stop Spark", "Always call spark.stop() when done"),
]

for mistake, solution in mistakes:
    console.print(f"[red]✗[/red] {mistake:35} [green]→[/green] {solution}")

# Quick Commands Reference
console.print("\n[bold]⚡ QUICK COMMANDS[/bold]")
console.print("=" * 80)

commands = """
# Initialize Spark
spark = SparkSession.builder.appName("MyApp").master("local[*]").getOrCreate()

# Read Data
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
df = spark.read.parquet("path/to/file.parquet")

# Basic Operations
df.show(10)                    # Display 10 rows
df.printSchema()               # Show schema
df.count()                     # Count rows
df.columns                     # List columns
df.describe().show()           # Summary statistics

# Write Data
df.write.mode("overwrite").parquet("output/path")
df.write.mode("append").csv("output/path", header=True)

# Performance
df.cache()                     # Cache in memory
df.explain()                   # Show execution plan
df.repartition(10)             # Change partitions
spark.stop()                   # Stop session
"""
console.print(f"[green]{commands}[/green]")

console.print("\n" + "=" * 80)
console.print("✅ You're ready for PySpark interviews!", style="bold green")
console.print("=" * 80)



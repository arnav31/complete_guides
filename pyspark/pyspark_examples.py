"""
PYSPARK EXAMPLES - Your Working File
Practice and experiment with PySpark here
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from rich.console import Console

console = Console()

# Initialize Spark
console.print("[bold yellow]🔥 Initializing Spark Session...[/bold yellow]")
spark = SparkSession.builder \
    .appName("PySpark Examples") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
console.print("[bold green]✅ Spark initialized![/bold green]\n")

console.print("[bold green]🎯 PYSPARK PRACTICE EXAMPLES[/bold green]")
console.print("=" * 80)

# Sample data
data = [
    (1, "Alice", 25, 50000, "IT", "2020-01-15"),
    (2, "Bob", 30, 60000, "HR", "2019-06-20"),
    (3, "Charlie", 35, 75000, "IT", "2018-03-10"),
    (4, "David", 28, 55000, "Finance", "2021-11-05"),
    (5, "Eve", 32, 70000, "HR", "2020-09-12")
]
columns = ["id", "name", "age", "salary", "department", "join_date"]
df = spark.createDataFrame(data, columns)

# =============================================================================
# BASIC OPERATIONS
# =============================================================================

console.print("\n[bold cyan]📚 BASIC OPERATIONS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 1: Display DataFrame[/yellow]")
df.show()

console.print("\n[yellow]Example 2: Show Schema[/yellow]")
df.printSchema()

console.print("\n[yellow]Example 3: Select Specific Columns[/yellow]")
df.select("name", "age", "department").show()

console.print("\n[yellow]Example 4: Filter Rows[/yellow]")
df.filter(col("age") > 30).show()

console.print("\n[yellow]Example 5: Add New Column[/yellow]")
df.withColumn("bonus", col("salary") * 0.1).show()

# =============================================================================
# AGGREGATIONS
# =============================================================================

console.print("\n[bold cyan]📊 AGGREGATIONS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 6: Count Total Rows[/yellow]")
console.print(f"Total rows: [green]{df.count()}[/green]")

console.print("\n[yellow]Example 7: Group By and Aggregate[/yellow]")
df.groupBy("department").agg(
    count("*").alias("count"),
    avg("salary").alias("avg_salary")
).show()

console.print("\n[yellow]Example 8: Multiple Aggregations[/yellow]")
df.agg(
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary")
).show()

# =============================================================================
# JOINS
# =============================================================================

console.print("\n[bold cyan]🔗 JOINS[/bold cyan]")
console.print("-" * 80)

# Create second DataFrame for joining
dept_data = [(1, "IT", "Technology"), (2, "HR", "Human Resources"), (3, "Finance", "Financial")]
dept_df = spark.createDataFrame(dept_data, ["dept_id", "dept_name", "description"])

console.print("\n[yellow]Example 9: Inner Join[/yellow]")
df.join(dept_df, df.department == dept_df.dept_name, "inner") \
  .select("name", "department", "description") \
  .show()

console.print("\n[yellow]Example 10: Left Join[/yellow]")
df.join(dept_df, df.department == dept_df.dept_name, "left") \
  .select("name", "department", "description") \
  .show()

# =============================================================================
# STRING FUNCTIONS
# =============================================================================

console.print("\n[bold cyan]🔤 STRING FUNCTIONS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 11: String Transformations[/yellow]")
df.select(
    col("name"),
    upper(col("name")).alias("upper"),
    lower(col("name")).alias("lower"),
    length(col("name")).alias("length")
).show()

console.print("\n[yellow]Example 12: Concatenate Strings[/yellow]")
df.select(
    concat(col("name"), lit(" - "), col("department")).alias("full_info")
).show()

console.print("\n[yellow]Example 13: Substring[/yellow]")
df.select(
    col("name"),
    substring(col("name"), 1, 3).alias("first_3_chars")
).show()

# =============================================================================
# DATE FUNCTIONS
# =============================================================================

console.print("\n[bold cyan]📅 DATE FUNCTIONS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 14: Convert to Date[/yellow]")
df_with_date = df.withColumn("join_date", to_date(col("join_date")))
df_with_date.select("name", "join_date").show()

console.print("\n[yellow]Example 15: Extract Date Parts[/yellow]")
df_with_date.select(
    col("name"),
    col("join_date"),
    year(col("join_date")).alias("year"),
    month(col("join_date")).alias("month"),
    dayofmonth(col("join_date")).alias("day")
).show()

console.print("\n[yellow]Example 16: Date Arithmetic[/yellow]")
df_with_date.select(
    col("name"),
    col("join_date"),
    date_add(col("join_date"), 365).alias("one_year_later"),
    datediff(current_date(), col("join_date")).alias("days_since_joining")
).show()

# =============================================================================
# CONDITIONAL LOGIC
# =============================================================================

console.print("\n[bold cyan]🔀 CONDITIONAL LOGIC[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 17: When/Otherwise (Case When)[/yellow]")
df.withColumn("salary_category",
    when(col("salary") > 65000, "High")
    .when(col("salary") > 55000, "Medium")
    .otherwise("Low")
).select("name", "salary", "salary_category").show()

console.print("\n[yellow]Example 18: Coalesce (Handle Nulls)[/yellow]")
df_nulls = df.withColumn("bonus", lit(None).cast("integer"))
df_nulls.select(
    col("name"),
    col("bonus"),
    coalesce(col("bonus"), lit(0)).alias("bonus_or_zero")
).show()

# =============================================================================
# WINDOW FUNCTIONS
# =============================================================================

console.print("\n[bold cyan]🪟 WINDOW FUNCTIONS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 19: Row Number[/yellow]")
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("rank_in_dept", row_number().over(window_spec)) \
  .select("name", "department", "salary", "rank_in_dept") \
  .show()

console.print("\n[yellow]Example 20: Rank and Dense Rank[/yellow]")
df.withColumn("rank", rank().over(window_spec)) \
  .withColumn("dense_rank", dense_rank().over(window_spec)) \
  .select("name", "department", "salary", "rank", "dense_rank") \
  .show()

console.print("\n[yellow]Example 21: Lag and Lead[/yellow]")
df.withColumn("prev_salary", lag("salary", 1).over(window_spec)) \
  .withColumn("next_salary", lead("salary", 1).over(window_spec)) \
  .select("name", "department", "salary", "prev_salary", "next_salary") \
  .show()

console.print("\n[yellow]Example 22: Running Total[/yellow]")
window_running = Window.partitionBy("department").orderBy("id").rowsBetween(Window.unboundedPreceding, 0)
df.withColumn("running_total", sum("salary").over(window_running)) \
  .select("department", "name", "salary", "running_total") \
  .show()

# =============================================================================
# NULL HANDLING
# =============================================================================

console.print("\n[bold cyan]🔍 NULL HANDLING[/bold cyan]")
console.print("-" * 80)

# Create DataFrame with nulls
null_data = [(1, "Alice", 25, 50000), (2, "Bob", None, 60000), (3, None, 35, None)]
df_nulls = spark.createDataFrame(null_data, ["id", "name", "age", "salary"])

console.print("\n[yellow]Example 23: Filter Null Values[/yellow]")
console.print("Rows with null age:")
df_nulls.filter(col("age").isNull()).show()

console.print("\n[yellow]Example 24: Filter Non-Null Values[/yellow]")
df_nulls.filter(col("age").isNotNull()).show()

console.print("\n[yellow]Example 25: Drop Rows with Nulls[/yellow]")
df_nulls.dropna().show()

console.print("\n[yellow]Example 26: Fill Null Values[/yellow]")
df_nulls.fillna({"age": 0, "salary": 0, "name": "Unknown"}).show()

# =============================================================================
# SQL OPERATIONS
# =============================================================================

console.print("\n[bold cyan]🗄️  SQL OPERATIONS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 27: Create Temp View and Query with SQL[/yellow]")
df.createOrReplaceTempView("employees")

result = spark.sql("""
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 60000
""")
result.show()

console.print("\n[yellow]Example 28: Complex SQL Query[/yellow]")
result = spark.sql("""
    SELECT 
        name,
        salary,
        CASE 
            WHEN salary > 65000 THEN 'High'
            WHEN salary > 55000 THEN 'Medium'
            ELSE 'Low'
        END as salary_category
    FROM employees
    WHERE age > 25
    ORDER BY salary DESC
""")
result.show()

# =============================================================================
# PERFORMANCE
# =============================================================================

console.print("\n[bold cyan]⚡ PERFORMANCE[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Example 29: Cache DataFrame[/yellow]")
df_cached = df.cache()
console.print(f"Cached. Row count: [green]{df_cached.count()}[/green]")

console.print("\n[yellow]Example 30: Check Partitions[/yellow]")
console.print(f"Number of partitions: [green]{df.rdd.getNumPartitions()}[/green]")

console.print("\n[yellow]Example 31: Repartition[/yellow]")
df_repart = df.repartition(4)
console.print(f"After repartition: [green]{df_repart.rdd.getNumPartitions()}[/green] partitions")

# =============================================================================
# PRACTICAL INTERVIEW PROBLEMS
# =============================================================================

console.print("\n[bold cyan]💼 PRACTICAL INTERVIEW PROBLEMS[/bold cyan]")
console.print("-" * 80)

console.print("\n[yellow]Problem 1: Find Top N Per Group[/yellow]")
console.print("Task: Find top 2 highest salaries in each department")
window_top = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("rank", row_number().over(window_top)) \
  .filter(col("rank") <= 2) \
  .select("department", "name", "salary", "rank") \
  .show()

console.print("\n[yellow]Problem 2: Calculate Cumulative Sum[/yellow]")
console.print("Task: Calculate running total of salaries by department")
window_running = Window.partitionBy("department").orderBy("id").rowsBetween(Window.unboundedPreceding, 0)
df.withColumn("cumulative_salary", sum("salary").over(window_running)) \
  .select("department", "name", "salary", "cumulative_salary") \
  .show()

console.print("\n[yellow]Problem 3: Find Duplicates[/yellow]")
console.print("Task: Find departments with more than one employee")
df.groupBy("department").count().filter(col("count") > 1).show()

console.print("\n[yellow]Problem 4: Pivot Data[/yellow]")
console.print("Task: Transform departments into columns")
df.groupBy("age").pivot("department").agg(sum("salary")).show()

console.print("\n[yellow]Problem 5: Calculate Percentile[/yellow]")
console.print("Task: Find median salary")
df.select(percentile_approx("salary", 0.5).alias("median_salary")).show()

# =============================================================================
# PRACTICE AREA
# =============================================================================

console.print("\n[bold cyan]✏️  YOUR PRACTICE AREA[/bold cyan]")
console.print("-" * 80)
console.print("\n[yellow]Add your own examples below and experiment![/yellow]\n")

# Your practice code here
# Example:
# df.filter(col("age") > 28).show()

console.print("\n" + "=" * 80)
console.print("[bold green]✅ Great practice! Keep experimenting with PySpark![/bold green]")
console.print("=" * 80)

# Stop Spark
spark.stop()
console.print("\n[bold yellow]🔥 Spark Session stopped[/bold yellow]")



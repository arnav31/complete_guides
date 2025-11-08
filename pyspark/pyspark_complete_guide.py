"""
PYSPARK COMPLETE GUIDE - From Basic to Advanced
A comprehensive reference for interview preparation
Each function includes: Description + Example + Output
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from rich.console import Console
from rich.table import Table
from rich import box

# Initialize Rich console for beautiful output
console = Console()

# Initialize Spark Session
console.print("\n[bold yellow]🔥 Initializing Spark Session...[/bold yellow]")
spark = SparkSession.builder \
    .appName("PySpark Complete Guide") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
console.print("[bold green]✅ Spark Session initialized successfully![/bold green]\n")

print("=" * 80)
print("PYSPARK COMPLETE GUIDE - Interview Preparation")
print("=" * 80)

# =============================================================================
# 1. DATAFRAME CREATION
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("1. DATAFRAME CREATION", style="bold green")
console.print("=" * 80, style="bold")

# 1.1 Create DataFrame from list of tuples
console.print("\n[cyan]--- 1.1 Create from List of Tuples ---[/cyan]")
data = [
    (1, "Alice", 25, 50000, "IT"),
    (2, "Bob", 30, 60000, "HR"),
    (3, "Charlie", 35, 75000, "IT"),
    (4, "David", 28, 55000, "Finance"),
    (5, "Eve", 32, 70000, "HR")
]
columns = ["id", "name", "age", "salary", "department"]
df = spark.createDataFrame(data, columns)
console.print("[dim]Description: Create DataFrame from Python list[/dim]")
df.show()

# 1.2 Create DataFrame with explicit schema
console.print("\n[cyan]--- 1.2 Create with Explicit Schema ---[/cyan]")
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", IntegerType(), True),
    StructField("department", StringType(), True)
])
df_with_schema = spark.createDataFrame(data, schema)
console.print("[dim]Description: Define schema explicitly for type safety[/dim]")
df_with_schema.printSchema()

# 1.3 Create DataFrame from dictionary
console.print("\n[cyan]--- 1.3 Create from Dictionary ---[/cyan]")
data_dict = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 35}
]
df_dict = spark.createDataFrame(data_dict)
console.print("[dim]Description: Create from list of dictionaries[/dim]")
df_dict.show()

# 1.4 Create empty DataFrame
console.print("\n[cyan]--- 1.4 Create Empty DataFrame ---[/cyan]")
empty_df = spark.createDataFrame([], schema)
console.print("[dim]Description: Create empty DataFrame with schema[/dim]")
console.print(f"Empty DataFrame created with {empty_df.count()} rows")

# =============================================================================
# 2. READING & WRITING DATA
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("2. READING & WRITING DATA", style="bold green")
console.print("=" * 80, style="bold")

# 2.1 Write to CSV
console.print("\n[cyan]--- 2.1 Write to CSV ---[/cyan]")
df.write.mode("overwrite").csv("/tmp/pyspark_data.csv", header=True)
console.print("[dim]Description: Write DataFrame to CSV with header[/dim]")
console.print("[green]✓ Data written to /tmp/pyspark_data.csv[/green]")

# 2.2 Read from CSV
console.print("\n[cyan]--- 2.2 Read from CSV ---[/cyan]")
df_csv = spark.read.csv("/tmp/pyspark_data.csv", header=True, inferSchema=True)
console.print("[dim]Description: Read CSV with header and infer schema[/dim]")
df_csv.show(3)

# 2.3 Write to Parquet
console.print("\n[cyan]--- 2.3 Write to Parquet ---[/cyan]")
df.write.mode("overwrite").parquet("/tmp/pyspark_data.parquet")
console.print("[dim]Description: Write to Parquet (columnar format)[/dim]")
console.print("[green]✓ Data written to /tmp/pyspark_data.parquet[/green]")

# 2.4 Read from Parquet
console.print("\n[cyan]--- 2.4 Read from Parquet ---[/cyan]")
df_parquet = spark.read.parquet("/tmp/pyspark_data.parquet")
console.print("[dim]Description: Read Parquet file (preserves schema)[/dim]")
console.print(f"Rows read: [green]{df_parquet.count()}[/green]")

# 2.5 Write to JSON
console.print("\n[cyan]--- 2.5 Write to JSON ---[/cyan]")
df.write.mode("overwrite").json("/tmp/pyspark_data.json")
console.print("[dim]Description: Write DataFrame to JSON[/dim]")
console.print("[green]✓ Data written to /tmp/pyspark_data.json[/green]")

# =============================================================================
# 3. BASIC TRANSFORMATIONS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("3. BASIC TRANSFORMATIONS", style="bold green")
console.print("=" * 80, style="bold")

# 3.1 Select columns
console.print("\n[cyan]--- 3.1 select() - Select specific columns ---[/cyan]")
df.select("name", "age", "department").show(3)
console.print("[dim]Description: Select specific columns from DataFrame[/dim]")

# 3.2 Select with column expressions
console.print("\n[cyan]--- 3.2 select() with col() ---[/cyan]")
df.select(col("name"), col("salary") * 1.1).show(3)
console.print("[dim]Description: Use col() for column expressions[/dim]")

# 3.3 Filter rows
console.print("\n[cyan]--- 3.3 filter() / where() - Filter rows ---[/cyan]")
df.filter(col("age") > 30).show()
console.print("[dim]Description: Filter rows based on condition[/dim]")

# 3.4 Multiple filter conditions
console.print("\n[cyan]--- 3.4 Multiple Filter Conditions ---[/cyan]")
df.filter((col("age") > 25) & (col("department") == "IT")).show()
console.print("[dim]Description: Combine conditions with & (AND) | (OR)[/dim]")

# 3.5 Add new column
console.print("\n[cyan]--- 3.5 withColumn() - Add/Modify column ---[/cyan]")
df_bonus = df.withColumn("bonus", col("salary") * 0.1)
df_bonus.show(3)
console.print("[dim]Description: Add new column with calculation[/dim]")

# 3.6 Rename column
console.print("\n[cyan]--- 3.6 withColumnRenamed() - Rename column ---[/cyan]")
df_renamed = df.withColumnRenamed("name", "employee_name")
df_renamed.show(3)
console.print("[dim]Description: Rename existing column[/dim]")

# 3.7 Drop columns
console.print("\n[cyan]--- 3.7 drop() - Remove columns ---[/cyan]")
df_dropped = df.drop("age", "department")
df_dropped.show(3)
console.print("[dim]Description: Drop one or more columns[/dim]")

# 3.8 Drop duplicates
console.print("\n[cyan]--- 3.8 dropDuplicates() / distinct() ---[/cyan]")
df_unique = df.dropDuplicates(["department"])
df_unique.show()
console.print("[dim]Description: Remove duplicate rows based on columns[/dim]")

# 3.9 Sort/Order
console.print("\n[cyan]--- 3.9 orderBy() / sort() - Sort DataFrame ---[/cyan]")
df.orderBy(col("salary").desc()).show(3)
console.print("[dim]Description: Sort by one or more columns[/dim]")

# 3.10 Limit rows
console.print("\n[cyan]--- 3.10 limit() - Limit number of rows ---[/cyan]")
df.limit(3).show()
console.print("[dim]Description: Return only first n rows[/dim]")

# =============================================================================
# 4. AGGREGATIONS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("4. AGGREGATIONS", style="bold green")
console.print("=" * 80, style="bold")

# 4.1 Count
console.print("\n[cyan]--- 4.1 count() - Count rows ---[/cyan]")
total_count = df.count()
console.print(f"[green]Total rows: {total_count}[/green]")
console.print("[dim]Description: Count total number of rows[/dim]")

# 4.2 Basic aggregations
console.print("\n[cyan]--- 4.2 agg() - Multiple aggregations ---[/cyan]")
df.agg(
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary"),
    sum("salary").alias("total_salary")
).show()
console.print("[dim]Description: Perform multiple aggregations at once[/dim]")

# 4.3 GroupBy
console.print("\n[cyan]--- 4.3 groupBy() - Group and aggregate ---[/cyan]")
df.groupBy("department").agg(
    count("*").alias("employee_count"),
    avg("salary").alias("avg_salary")
).show()
console.print("[dim]Description: Group by column and aggregate[/dim]")

# 4.4 GroupBy with multiple aggregations
console.print("\n[cyan]--- 4.4 GroupBy with Multiple Aggregations ---[/cyan]")
df.groupBy("department").agg(
    count("*").alias("count"),
    avg("age").alias("avg_age"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary")
).show()
console.print("[dim]Description: Multiple aggregations per group[/dim]")

# 4.5 GroupBy with having
console.print("\n[cyan]--- 4.5 GroupBy with Having (filter groups) ---[/cyan]")
df.groupBy("department") \
  .agg(avg("salary").alias("avg_salary")) \
  .filter(col("avg_salary") > 60000) \
  .show()
console.print("[dim]Description: Filter groups after aggregation[/dim]")

# =============================================================================
# 5. JOINS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("5. JOINS", style="bold green")
console.print("=" * 80, style="bold")

# Create second DataFrame for joins
dept_data = [
    (1, "IT", "Technology"),
    (2, "HR", "Human Resources"),
    (3, "Finance", "Financial Operations"),
    (4, "Marketing", "Marketing & Sales")
]
dept_df = spark.createDataFrame(dept_data, ["dept_id", "dept_name", "description"])

# 5.1 Inner Join
console.print("\n[cyan]--- 5.1 join() - Inner Join ---[/cyan]")
df.join(dept_df, df.department == dept_df.dept_name, "inner") \
  .select("name", "department", "description") \
  .show()
console.print("[dim]Description: Returns only matching rows from both DataFrames[/dim]")

# 5.2 Left Join
console.print("\n[cyan]--- 5.2 Left Join ---[/cyan]")
df.join(dept_df, df.department == dept_df.dept_name, "left") \
  .select("name", "department", "description") \
  .show()
console.print("[dim]Description: Returns all rows from left, matching from right[/dim]")

# 5.3 Right Join
console.print("\n[cyan]--- 5.3 Right Join ---[/cyan]")
df.join(dept_df, df.department == dept_df.dept_name, "right") \
  .select("name", "dept_name", "description") \
  .show()
console.print("[dim]Description: Returns all rows from right, matching from left[/dim]")

# 5.4 Full Outer Join
console.print("\n[cyan]--- 5.4 Full Outer Join ---[/cyan]")
df.join(dept_df, df.department == dept_df.dept_name, "outer") \
  .select("name", "department", "dept_name", "description") \
  .show()
console.print("[dim]Description: Returns all rows from both DataFrames[/dim]")

# 5.5 Left Semi Join
console.print("\n[cyan]--- 5.5 Left Semi Join ---[/cyan]")
df.join(dept_df, df.department == dept_df.dept_name, "left_semi") \
  .show()
console.print("[dim]Description: Returns rows from left that have match in right[/dim]")

# 5.6 Left Anti Join
console.print("\n[cyan]--- 5.6 Left Anti Join ---[/cyan]")
df.join(dept_df, df.department == dept_df.dept_name, "left_anti") \
  .show()
console.print("[dim]Description: Returns rows from left with NO match in right[/dim]")

# =============================================================================
# 6. COLUMN FUNCTIONS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("6. COLUMN FUNCTIONS", style="bold green")
console.print("=" * 80, style="bold")

# 6.1 String functions
console.print("\n[cyan]--- 6.1 String Functions ---[/cyan]")
df.select(
    col("name"),
    upper(col("name")).alias("upper_name"),
    lower(col("name")).alias("lower_name"),
    length(col("name")).alias("name_length")
).show(3)
console.print("[dim]Description: upper(), lower(), length() for strings[/dim]")

# 6.2 Substring
console.print("\n[cyan]--- 6.2 substring() - Extract substring ---[/cyan]")
df.select(
    col("name"),
    substring(col("name"), 1, 3).alias("first_3_chars")
).show(3)
console.print("[dim]Description: Extract substring (1-indexed)[/dim]")

# 6.3 Concatenate
console.print("\n[cyan]--- 6.3 concat() - Concatenate columns ---[/cyan]")
df.select(
    concat(col("name"), lit(" - "), col("department")).alias("full_info")
).show(3)
console.print("[dim]Description: Concatenate multiple columns/literals[/dim]")

# 6.4 Replace/Regex
console.print("\n[cyan]--- 6.4 regexp_replace() - Replace with regex ---[/cyan]")
df.select(
    col("name"),
    regexp_replace(col("name"), "[aeiou]", "*").alias("censored")
).show(3)
console.print("[dim]Description: Replace using regular expression[/dim]")

# 6.5 When/Otherwise (case when)
console.print("\n[cyan]--- 6.5 when() / otherwise() - Conditional logic ---[/cyan]")
df.withColumn("salary_level",
    when(col("salary") > 65000, "High")
    .when(col("salary") > 55000, "Medium")
    .otherwise("Low")
).select("name", "salary", "salary_level").show()
console.print("[dim]Description: SQL CASE WHEN equivalent[/dim]")

# 6.6 Cast types
console.print("\n[cyan]--- 6.6 cast() - Type conversion ---[/cyan]")
df.select(
    col("salary").cast("string").alias("salary_str"),
    col("age").cast("double").alias("age_double")
).printSchema()
console.print("[dim]Description: Convert column to different data type[/dim]")

# 6.7 Null handling
console.print("\n[cyan]--- 6.7 Null Handling Functions ---[/cyan]")
df_nulls = df.withColumn("bonus", lit(None).cast("integer"))
df_nulls.select(
    col("name"),
    col("bonus"),
    coalesce(col("bonus"), lit(0)).alias("bonus_coalesced"),
    when(col("bonus").isNull(), "No bonus").otherwise("Has bonus").alias("status")
).show(3)
console.print("[dim]Description: isNull(), isNotNull(), coalesce()[/dim]")

# =============================================================================
# 7. DATE & TIME FUNCTIONS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("7. DATE & TIME FUNCTIONS", style="bold green")
console.print("=" * 80, style="bold")

# Create DataFrame with dates
date_data = [
    (1, "2024-01-15", "2024-01-15 10:30:00"),
    (2, "2024-02-20", "2024-02-20 14:45:00"),
    (3, "2024-03-25", "2024-03-25 09:15:00")
]
date_df = spark.createDataFrame(date_data, ["id", "date_str", "timestamp_str"])

# 7.1 Current date/timestamp
console.print("\n[cyan]--- 7.1 current_date() / current_timestamp() ---[/cyan]")
date_df.select(
    current_date().alias("today"),
    current_timestamp().alias("now")
).show(1, truncate=False)
console.print("[dim]Description: Get current date and timestamp[/dim]")

# 7.2 Convert to date/timestamp
console.print("\n[cyan]--- 7.2 to_date() / to_timestamp() ---[/cyan]")
date_df = date_df.withColumn("date", to_date(col("date_str"))) \
                 .withColumn("timestamp", to_timestamp(col("timestamp_str")))
date_df.select("date", "timestamp").show(3, truncate=False)
console.print("[dim]Description: Convert string to date/timestamp[/dim]")

# 7.3 Extract date parts
console.print("\n[cyan]--- 7.3 Extract Date Parts ---[/cyan]")
date_df.select(
    col("date"),
    year(col("date")).alias("year"),
    month(col("date")).alias("month"),
    dayofmonth(col("date")).alias("day"),
    dayofweek(col("date")).alias("day_of_week")
).show(3)
console.print("[dim]Description: year(), month(), dayofmonth(), dayofweek()[/dim]")

# 7.4 Date arithmetic
console.print("\n[cyan]--- 7.4 Date Arithmetic ---[/cyan]")
date_df.select(
    col("date"),
    date_add(col("date"), 7).alias("plus_7_days"),
    date_sub(col("date"), 7).alias("minus_7_days"),
    datediff(current_date(), col("date")).alias("days_ago")
).show(3)
console.print("[dim]Description: date_add(), date_sub(), datediff()[/dim]")

# 7.5 Format date
console.print("\n[cyan]--- 7.5 date_format() - Format date as string ---[/cyan]")
date_df.select(
    col("date"),
    date_format(col("date"), "yyyy-MM-dd").alias("iso_format"),
    date_format(col("date"), "dd/MM/yyyy").alias("eu_format"),
    date_format(col("date"), "MMM dd, yyyy").alias("readable")
).show(3, truncate=False)
console.print("[dim]Description: Format date using pattern[/dim]")

# =============================================================================
# 8. WINDOW FUNCTIONS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("8. WINDOW FUNCTIONS", style="bold green")
console.print("=" * 80, style="bold")

# 8.1 Row number
console.print("\n[cyan]--- 8.1 row_number() - Assign row numbers ---[/cyan]")
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("row_num", row_number().over(window_spec)) \
  .select("name", "department", "salary", "row_num") \
  .show()
console.print("[dim]Description: Assign sequential numbers within partitions[/dim]")

# 8.2 Rank
console.print("\n[cyan]--- 8.2 rank() / dense_rank() ---[/cyan]")
df.withColumn("rank", rank().over(window_spec)) \
  .withColumn("dense_rank", dense_rank().over(window_spec)) \
  .select("name", "department", "salary", "rank", "dense_rank") \
  .show()
console.print("[dim]Description: rank() has gaps, dense_rank() doesn't[/dim]")

# 8.3 Lag and Lead
console.print("\n[cyan]--- 8.3 lag() / lead() - Access previous/next row ---[/cyan]")
df.withColumn("prev_salary", lag("salary", 1).over(window_spec)) \
  .withColumn("next_salary", lead("salary", 1).over(window_spec)) \
  .select("name", "department", "salary", "prev_salary", "next_salary") \
  .show()
console.print("[dim]Description: Access values from adjacent rows[/dim]")

# 8.4 Running total
console.print("\n[cyan]--- 8.4 Running Total / Cumulative Sum ---[/cyan]")
window_running = Window.partitionBy("department").orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn("running_total", sum("salary").over(window_running)) \
  .select("name", "department", "salary", "running_total") \
  .show()
console.print("[dim]Description: Calculate cumulative sum[/dim]")

# 8.5 Moving average
console.print("\n[cyan]--- 8.5 Moving Average ---[/cyan]")
window_moving = Window.partitionBy("department").orderBy("id").rowsBetween(-1, 1)
df.withColumn("moving_avg", avg("salary").over(window_moving)) \
  .select("name", "department", "salary", "moving_avg") \
  .show()
console.print("[dim]Description: Calculate moving average over window[/dim]")

# =============================================================================
# 9. USER DEFINED FUNCTIONS (UDFs)
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("9. USER DEFINED FUNCTIONS (UDFs)", style="bold green")
console.print("=" * 80, style="bold")

# 9.1 Simple UDF
console.print("\n[cyan]--- 9.1 Create and Use UDF ---[/cyan]")
from pyspark.sql.functions import udf

def categorize_age(age):
    if age < 30:
        return "Young"
    elif age < 35:
        return "Middle"
    else:
        return "Senior"

age_category_udf = udf(categorize_age, StringType())
df.withColumn("age_category", age_category_udf(col("age"))) \
  .select("name", "age", "age_category") \
  .show()
console.print("[dim]Description: Create custom Python function as UDF[/dim]")

# 9.2 UDF with multiple inputs
console.print("\n[cyan]--- 9.2 UDF with Multiple Inputs ---[/cyan]")
def calculate_bonus(salary, age):
    if age > 30:
        return salary * 0.15
    else:
        return salary * 0.10

bonus_udf = udf(calculate_bonus, IntegerType())
df.withColumn("calculated_bonus", bonus_udf(col("salary"), col("age"))) \
  .select("name", "salary", "age", "calculated_bonus") \
  .show()
console.print("[dim]Description: UDF with multiple input columns[/dim]")

# 9.3 pandas_udf (Vectorized UDF) - More efficient
console.print("\n[cyan]--- 9.3 pandas_udf() - Vectorized UDF ---[/cyan]")
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(IntegerType())
def calculate_bonus_vectorized(salary: pd.Series, age: pd.Series) -> pd.Series:
    return (salary * 0.15).where(age > 30, salary * 0.10).astype(int)

df.withColumn("bonus_vectorized", calculate_bonus_vectorized(col("salary"), col("age"))) \
  .select("name", "salary", "age", "bonus_vectorized") \
  .show()
console.print("[dim]Description: Vectorized UDF for better performance[/dim]")

# =============================================================================
# 10. SQL OPERATIONS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("10. SQL OPERATIONS", style="bold green")
console.print("=" * 80, style="bold")

# 10.1 Create temp view
console.print("\n[cyan]--- 10.1 createOrReplaceTempView() - SQL interface ---[/cyan]")
df.createOrReplaceTempView("employees")
console.print("[dim]Description: Create temporary view for SQL queries[/dim]")

# 10.2 SQL SELECT
console.print("\n[cyan]--- 10.2 spark.sql() - Execute SQL queries ---[/cyan]")
result = spark.sql("""
    SELECT name, department, salary
    FROM employees
    WHERE salary > 60000
    ORDER BY salary DESC
""")
result.show()
console.print("[dim]Description: Use SQL syntax to query DataFrames[/dim]")

# 10.3 SQL Aggregation
console.print("\n[cyan]--- 10.3 SQL Aggregation ---[/cyan]")
result = spark.sql("""
    SELECT 
        department,
        COUNT(*) as employee_count,
        AVG(salary) as avg_salary,
        MAX(salary) as max_salary
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 60000
""")
result.show()
console.print("[dim]Description: Complex SQL with GROUP BY and HAVING[/dim]")

# 10.4 SQL Join
console.print("\n[cyan]--- 10.4 SQL Join ---[/cyan]")
dept_df.createOrReplaceTempView("departments")
result = spark.sql("""
    SELECT e.name, e.department, d.description
    FROM employees e
    INNER JOIN departments d ON e.department = d.dept_name
""")
result.show()
console.print("[dim]Description: SQL JOIN between tables[/dim]")

# =============================================================================
# 11. HANDLING NULL VALUES
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("11. HANDLING NULL VALUES", style="bold green")
console.print("=" * 80, style="bold")

# Create DataFrame with nulls
null_data = [
    (1, "Alice", 25, 50000),
    (2, "Bob", None, 60000),
    (3, None, 35, None),
    (4, "David", 28, 55000)
]
df_nulls = spark.createDataFrame(null_data, ["id", "name", "age", "salary"])

# 11.1 Filter null values
console.print("\n[cyan]--- 11.1 Filter Null / Non-Null Values ---[/cyan]")
console.print("Rows with null age:")
df_nulls.filter(col("age").isNull()).show()
console.print("Rows with non-null age:")
df_nulls.filter(col("age").isNotNull()).show()
console.print("[dim]Description: Use isNull() and isNotNull()[/dim]")

# 11.2 Drop null values
console.print("\n[cyan]--- 11.2 dropna() - Drop rows with nulls ---[/cyan]")
df_nulls.dropna().show()
console.print("[dim]Description: Drop rows with any null values[/dim]")

# 11.3 Drop with threshold
console.print("\n[cyan]--- 11.3 dropna(thresh=n) - Drop if < n non-nulls ---[/cyan]")
df_nulls.dropna(thresh=3).show()
console.print("[dim]Description: Keep rows with at least n non-null values[/dim]")

# 11.4 Fill null values
console.print("\n[cyan]--- 11.4 fillna() - Fill null values ---[/cyan]")
df_nulls.fillna({"age": 0, "salary": 0, "name": "Unknown"}).show()
console.print("[dim]Description: Replace nulls with specified values[/dim]")

# 11.5 Replace values
console.print("\n[cyan]--- 11.5 replace() - Replace specific values ---[/cyan]")
df_nulls.replace({"Alice": "Alice Smith"}, subset=["name"]).show()
console.print("[dim]Description: Replace specific values in columns[/dim]")

# =============================================================================
# 12. PERFORMANCE & OPTIMIZATION
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("12. PERFORMANCE & OPTIMIZATION", style="bold green")
console.print("=" * 80, style="bold")

# 12.1 Cache
console.print("\n[cyan]--- 12.1 cache() / persist() - Cache DataFrame ---[/cyan]")
df_cached = df.cache()
console.print("[dim]Description: Cache DataFrame in memory for reuse[/dim]")
console.print(f"[green]DataFrame cached. Count: {df_cached.count()}[/green]")

# 12.2 Repartition
console.print("\n[cyan]--- 12.2 repartition() - Change partitions ---[/cyan]")
console.print(f"Original partitions: {df.rdd.getNumPartitions()}")
df_repartitioned = df.repartition(4)
console.print(f"After repartition: {df_repartitioned.rdd.getNumPartitions()}")
console.print("[dim]Description: Increase/decrease number of partitions[/dim]")

# 12.3 Coalesce
console.print("\n[cyan]--- 12.3 coalesce() - Reduce partitions ---[/cyan]")
df_coalesced = df_repartitioned.coalesce(2)
console.print(f"After coalesce: {df_coalesced.rdd.getNumPartitions()}")
console.print("[dim]Description: Efficiently reduce partitions (no shuffle)[/dim]")

# 12.4 Broadcast join
console.print("\n[cyan]--- 12.4 broadcast() - Broadcast small DataFrame ---[/cyan]")
from pyspark.sql.functions import broadcast
df.join(broadcast(dept_df), df.department == dept_df.dept_name, "inner") \
  .select("name", "department", "description") \
  .show(3)
console.print("[dim]Description: Broadcast small DataFrame to all nodes[/dim]")

# 12.5 Explain plan
console.print("\n[cyan]--- 12.5 explain() - View execution plan ---[/cyan]")
console.print("[dim]Description: View physical execution plan[/dim]")
df.filter(col("salary") > 60000).explain()

# =============================================================================
# 13. ACTIONS (Trigger Computation)
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("13. ACTIONS (Trigger Computation)", style="bold green")
console.print("=" * 80, style="bold")

console.print("\n[cyan]--- Common Actions ---[/cyan]")
console.print(f"• show() - Display DataFrame")
console.print(f"• count() - Count rows: [green]{df.count()}[/green]")
console.print(f"• collect() - Return all rows as list: [green]{len(df.collect())} rows[/green]")
console.print(f"• take(n) - Return first n rows: [green]{len(df.take(3))} rows[/green]")
console.print(f"• first() - Return first row: [green]{df.first()}[/green]")
console.print(f"• head(n) - Return first n rows: [green]{len(df.head(2))} rows[/green]")
console.print("[dim]Description: Actions trigger actual computation[/dim]")

# =============================================================================
# 14. COMMON INTERVIEW PROBLEMS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("14. COMMON INTERVIEW PROBLEMS", style="bold green")
console.print("=" * 80, style="bold")

# 14.1 Find top N per group
console.print("\n[cyan]--- 14.1 Top N Per Group ---[/cyan]")
window_top = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("rank", row_number().over(window_top)) \
  .filter(col("rank") <= 2) \
  .select("department", "name", "salary", "rank") \
  .show()
console.print("[dim]Problem: Find top 2 salaries in each department[/dim]")

# 14.2 Running total
console.print("\n[cyan]--- 14.2 Calculate Running Total ---[/cyan]")
window_running = Window.partitionBy("department").orderBy("id").rowsBetween(Window.unboundedPreceding, 0)
df.withColumn("running_total", sum("salary").over(window_running)) \
  .select("department", "name", "salary", "running_total") \
  .orderBy("department", "id") \
  .show()
console.print("[dim]Problem: Calculate cumulative sum by department[/dim]")

# 14.3 Find duplicates
console.print("\n[cyan]--- 14.3 Find Duplicate Records ---[/cyan]")
df.groupBy("department").count().filter(col("count") > 1).show()
console.print("[dim]Problem: Find departments with multiple employees[/dim]")

# 14.4 Pivot data
console.print("\n[cyan]--- 14.4 Pivot Data ---[/cyan]")
df.groupBy("age").pivot("department").agg(sum("salary")).show()
console.print("[dim]Problem: Transform rows to columns (pivot)[/dim]")

# 14.5 Unpivot data
console.print("\n[cyan]--- 14.5 Unpivot/Melt Data ---[/cyan]")
from pyspark.sql.functions import array, explode, struct, lit
df_pivot = df.groupBy("age").pivot("department").agg(sum("salary"))
# Note: PySpark doesn't have direct unpivot, need workaround
console.print("[dim]Problem: Transform columns back to rows[/dim]")

# 14.6 Calculate percentile
console.print("\n[cyan]--- 14.6 Calculate Percentile ---[/cyan]")
from pyspark.sql.functions import percentile_approx
df.select(percentile_approx("salary", 0.5).alias("median_salary")).show()
console.print("[dim]Problem: Find median (50th percentile)[/dim]")

# 14.7 Remove duplicate columns after join
console.print("\n[cyan]--- 14.7 Handle Duplicate Columns After Join ---[/cyan]")
df1 = df.select("id", "name", "department")
df2 = dept_df.select(col("dept_name").alias("department"), "description")
result = df1.join(df2, "department", "inner").select(df1["*"], df2.description)
result.show(3)
console.print("[dim]Problem: Avoid duplicate column names in join[/dim]")

# 14.8 Count null values per column
console.print("\n[cyan]--- 14.8 Count Null Values Per Column ---[/cyan]")
df_nulls.select([count(when(col(c).isNull(), c)).alias(c) for c in df_nulls.columns]).show()
console.print("[dim]Problem: Count nulls in each column[/dim]")

# 14.9 Sample data
console.print("\n[cyan]--- 14.9 sample() - Sample random rows ---[/cyan]")
df.sample(fraction=0.5, seed=42).show()
console.print("[dim]Problem: Get random sample of data[/dim]")

# 14.10 Union DataFrames
console.print("\n[cyan]--- 14.10 union() - Combine DataFrames vertically ---[/cyan]")
df1 = df.limit(2)
df2 = df.limit(2)
df1.union(df2).show()
console.print("[dim]Problem: Stack DataFrames (append rows)[/dim]")

console.print("\n" + "=" * 80, style="bold")
console.print("END OF PYSPARK COMPLETE GUIDE", style="bold green")
console.print("=" * 80, style="bold")
console.print("\n✅ You're now ready to ace PySpark interviews!", style="bold green")

# Stop Spark Session
spark.stop()
console.print("\n[bold yellow]🔥 Spark Session stopped[/bold yellow]")


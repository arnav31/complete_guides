"""
PANDAS COMPLETE GUIDE - From Basic to Advanced
A comprehensive reference for interview preparation
Each function includes: Example + Description + Output
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configure pandas display for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.precision', 2)

print("=" * 80)
print("PANDAS COMPLETE GUIDE - Interview Preparation")
print("=" * 80)

# =============================================================================
# 1. DATA CREATION
# =============================================================================
print("\n" + "=" * 80)
print("1. DATA CREATION")
print("=" * 80)

# 1.1 Creating DataFrame from dictionary
print("\n--- 1.1 pd.DataFrame(dict) - Create DataFrame from dictionary ---")
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 28, 32],
    "salary": [50000, 60000, 75000, 55000, 70000],
    "department": ["IT", "HR", "IT", "Finance", "HR"]
})
print("Description: Creates DataFrame from dict where keys=columns, values=lists")
print(df)

# 1.2 Creating DataFrame from list of lists
print("\n--- 1.2 pd.DataFrame(list) - Create from list of lists ---")
df_list = pd.DataFrame(
    [[1, "A", 100], [2, "B", 200], [3, "C", 300]],
    columns=["id", "letter", "value"]
)
print("Description: Creates DataFrame from nested lists with custom column names")
print(df_list)

# 1.3 Creating Series
print("\n--- 1.3 pd.Series() - Create a Series (1D labeled array) ---")
series = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"], name="numbers")
print("Description: Creates a 1D labeled array with custom index")
print(series)

# 1.4 Creating date range
print("\n--- 1.4 pd.date_range() - Create sequence of dates ---")
dates = pd.date_range(start="2024-01-01", periods=5, freq="D")
print("Description: Creates a sequence of dates (D=daily, M=monthly, H=hourly)")
print(dates)

# 1.5 Reading from CSV/Excel
print("\n--- 1.5 pd.read_csv() / pd.read_excel() - Read from files ---")
print("Description: Load data from CSV or Excel files")
print("Example: df = pd.read_csv('file.csv')")
print("         df = pd.read_excel('file.xlsx', sheet_name='Sheet1')")

# =============================================================================
# 2. VIEWING & INSPECTING DATA
# =============================================================================
print("\n" + "=" * 80)
print("2. VIEWING & INSPECTING DATA")
print("=" * 80)

# 2.1 Head and Tail
print("\n--- 2.1 df.head(n) / df.tail(n) - View first/last n rows ---")
print("Description: Shows first/last n rows (default n=5)")
print(df.head(3))

# 2.2 Info
print("\n--- 2.2 df.info() - Get DataFrame summary ---")
print("Description: Shows column types, non-null counts, memory usage")
print(df.info())

# 2.3 Describe
print("\n--- 2.3 df.describe() - Statistical summary ---")
print("Description: Shows count, mean, std, min, max, quartiles for numeric columns")
print(df.describe())

# 2.4 Shape, Size, Columns, Index
print("\n--- 2.4 Basic attributes ---")
print(f"df.shape: {df.shape} - Description: (rows, columns)")
print(f"df.size: {df.size} - Description: Total number of elements")
print(f"df.columns: {df.columns.tolist()} - Description: Column names")
print(f"df.index: {df.index.tolist()} - Description: Row indices")
print(f"df.dtypes:\n{df.dtypes}\nDescription: Data type of each column")

# 2.5 Value counts
print("\n--- 2.5 df['column'].value_counts() - Count unique values ---")
print("Description: Counts occurrences of each unique value")
print(df['department'].value_counts())

# 2.6 Unique and nunique
print("\n--- 2.6 df['column'].unique() / nunique() - Get unique values ---")
print(f"Unique departments: {df['department'].unique()}")
print(f"Number of unique departments: {df['department'].nunique()}")
print("Description: unique() returns array of unique values, nunique() returns count")

# =============================================================================
# 3. SELECTION & INDEXING
# =============================================================================
print("\n" + "=" * 80)
print("3. SELECTION & INDEXING")
print("=" * 80)

# 3.1 Select single column
print("\n--- 3.1 df['column'] - Select single column (returns Series) ---")
print("Description: Returns a Series (single column)")
print(df['name'])

# 3.2 Select multiple columns
print("\n--- 3.2 df[['col1', 'col2']] - Select multiple columns ---")
print("Description: Returns DataFrame with specified columns")
print(df[['name', 'age', 'department']])

# 3.3 loc - label-based indexing
print("\n--- 3.3 df.loc[row, col] - Label-based selection ---")
print("Description: Select by labels (row/column names)")
print("Single value:", df.loc[0, 'name'])
print("\nRow slice:")
print(df.loc[0:2, ['name', 'age']])

# 3.4 iloc - integer-based indexing
print("\n--- 3.4 df.iloc[row, col] - Integer position-based selection ---")
print("Description: Select by integer positions (0-indexed)")
print("Rows 1-3, Columns 0-2:")
print(df.iloc[1:3, 0:3])

# 3.5 at and iat - fast scalar access
print("\n--- 3.5 df.at[] / df.iat[] - Fast single value access ---")
print(f"df.at[1, 'age']: {df.at[1, 'age']} - Description: Fast label-based scalar")
print(f"df.iat[1, 2]: {df.iat[1, 2]} - Description: Fast integer-based scalar")

# 3.6 Boolean indexing
print("\n--- 3.6 df[condition] - Boolean/conditional indexing ---")
print("Description: Filter rows based on condition")
print(df[df['age'] > 30])

# 3.7 Multiple conditions
print("\n--- 3.7 Multiple conditions with & (AND) | (OR) ---")
print("Description: Combine conditions (use parentheses!)")
print(df[(df['age'] > 25) & (df['department'] == 'IT')])

# 3.8 isin - Filter by list of values
print("\n--- 3.8 df['col'].isin(values) - Filter by list ---")
print("Description: Check if values are in a list")
print(df[df['department'].isin(['IT', 'HR'])])

# 3.9 Query method
print("\n--- 3.9 df.query() - SQL-like filtering ---")
print("Description: Filter using string expression (cleaner syntax)")
print(df.query("age > 28 and salary >= 60000"))

# =============================================================================
# 4. ADDING, MODIFYING, DELETING COLUMNS/ROWS
# =============================================================================
print("\n" + "=" * 80)
print("4. ADDING, MODIFYING, DELETING COLUMNS/ROWS")
print("=" * 80)

# Make a copy for modifications
df_mod = df.copy()

# 4.1 Add new column
print("\n--- 4.1 df['new_col'] = values - Add new column ---")
df_mod['bonus'] = df_mod['salary'] * 0.1
print("Description: Creates new column with calculated values")
print(df_mod[['name', 'salary', 'bonus']])

# 4.2 Assign - add multiple columns
print("\n--- 4.2 df.assign() - Add multiple columns ---")
df_mod = df_mod.assign(
    tax=lambda x: x['salary'] * 0.2,
    net_salary=lambda x: x['salary'] - x['salary'] * 0.2
)
print("Description: Add multiple computed columns (functional style)")
print(df_mod[['name', 'salary', 'tax', 'net_salary']].head(3))

# 4.3 Drop columns
print("\n--- 4.3 df.drop(columns=[...]) - Remove columns ---")
df_temp = df_mod.drop(columns=['bonus', 'tax'])
print("Description: Remove specified columns (axis=1 or columns=)")
print(df_temp.columns.tolist())

# 4.4 Drop rows
print("\n--- 4.4 df.drop(index=[...]) - Remove rows ---")
df_temp = df_mod.drop(index=[0, 1])
print("Description: Remove rows by index labels")
print(df_temp)

# 4.5 Rename columns
print("\n--- 4.5 df.rename(columns={...}) - Rename columns ---")
df_temp = df.rename(columns={'name': 'employee_name', 'age': 'employee_age'})
print("Description: Rename specific columns using dictionary")
print(df_temp.columns.tolist())

# 4.6 Insert column at specific position
print("\n--- 4.6 df.insert(loc, column, value) - Insert column at position ---")
df_temp = df.copy()
df_temp.insert(1, 'employee_id', range(100, 105))
print("Description: Insert column at specific position (0-indexed)")
print(df_temp)

# =============================================================================
# 5. SORTING
# =============================================================================
print("\n" + "=" * 80)
print("5. SORTING")
print("=" * 80)

# 5.1 Sort by single column
print("\n--- 5.1 df.sort_values(by='column') - Sort by column ---")
print("Description: Sort rows by column values (ascending by default)")
print(df.sort_values(by='age'))

# 5.2 Sort by multiple columns
print("\n--- 5.2 Sort by multiple columns ---")
print("Description: Sort by multiple columns with different orders")
print(df.sort_values(by=['department', 'salary'], ascending=[True, False]))

# 5.3 Sort by index
print("\n--- 5.3 df.sort_index() - Sort by index ---")
df_temp = df.sample(frac=1)  # Shuffle
print("Description: Sort by row index")
print(df_temp.sort_index())

# =============================================================================
# 6. GROUPING & AGGREGATION
# =============================================================================
print("\n" + "=" * 80)
print("6. GROUPING & AGGREGATION")
print("=" * 80)

# 6.1 GroupBy with single aggregation
print("\n--- 6.1 df.groupby('column').agg() - Group and aggregate ---")
print("Description: Group by column and calculate statistics")
print(df.groupby('department')['salary'].mean())

# 6.2 GroupBy with multiple aggregations
print("\n--- 6.2 Multiple aggregations ---")
print("Description: Apply multiple aggregation functions")
print(df.groupby('department')['salary'].agg(['mean', 'min', 'max', 'count']))

# 6.3 GroupBy multiple columns
print("\n--- 6.3 Group by multiple columns ---")
df_temp = df.copy()
df_temp['experience'] = ['Junior', 'Senior', 'Senior', 'Junior', 'Senior']
result = df_temp.groupby(['department', 'experience'])['salary'].mean()
print("Description: Group by multiple columns")
print(result)

# 6.4 agg with dictionary (different function per column)
print("\n--- 6.4 df.groupby().agg({col: func}) - Different functions per column ---")
print("Description: Apply different aggregation to different columns")
result = df.groupby('department').agg({
    'salary': ['mean', 'sum'],
    'age': 'mean'
})
print(result)

# 6.5 Transform (keeps original shape)
print("\n--- 6.5 df.groupby().transform() - Apply function keeping shape ---")
df_temp = df.copy()
df_temp['dept_avg_salary'] = df_temp.groupby('department')['salary'].transform('mean')
print("Description: Add group statistics back to original DataFrame")
print(df_temp[['name', 'department', 'salary', 'dept_avg_salary']])

# 6.6 filter groups
print("\n--- 6.6 df.groupby().filter() - Filter groups by condition ---")
result = df.groupby('department').filter(lambda x: x['salary'].mean() > 60000)
print("Description: Keep only groups that satisfy condition")
print(result)

# =============================================================================
# 7. MERGING, JOINING, CONCATENATING
# =============================================================================
print("\n" + "=" * 80)
print("7. MERGING, JOINING, CONCATENATING")
print("=" * 80)

# Create sample DataFrames for merging
df1 = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'dept_id': [10, 20, 10, 30]
})

df2 = pd.DataFrame({
    'dept_id': [10, 20, 30, 40],
    'dept_name': ['Engineering', 'HR', 'Sales', 'Marketing']
})

# 7.1 Inner join
print("\n--- 7.1 pd.merge(df1, df2, on='key', how='inner') - Inner join ---")
result = pd.merge(df1, df2, on='dept_id', how='inner')
print("Description: Returns only matching rows from both DataFrames")
print(result)

# 7.2 Left join
print("\n--- 7.2 pd.merge(how='left') - Left join ---")
result = pd.merge(df1, df2, on='dept_id', how='left')
print("Description: Returns all rows from left, matching from right (NaN if no match)")
print(result)

# 7.3 Right join
print("\n--- 7.3 pd.merge(how='right') - Right join ---")
result = pd.merge(df1, df2, on='dept_id', how='right')
print("Description: Returns all rows from right, matching from left")
print(result)

# 7.4 Outer join
print("\n--- 7.4 pd.merge(how='outer') - Outer join (Full join) ---")
result = pd.merge(df1, df2, on='dept_id', how='outer')
print("Description: Returns all rows from both DataFrames")
print(result)

# 7.5 Concatenate vertically
print("\n--- 7.5 pd.concat([df1, df2], axis=0) - Stack vertically ---")
df_a = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_b = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result = pd.concat([df_a, df_b], axis=0, ignore_index=True)
print("Description: Stack DataFrames vertically (add rows)")
print(result)

# 7.6 Concatenate horizontally
print("\n--- 7.6 pd.concat([df1, df2], axis=1) - Stack horizontally ---")
result = pd.concat([df_a, df_b], axis=1)
print("Description: Stack DataFrames horizontally (add columns)")
print(result)

# 7.7 Join (index-based merge)
print("\n--- 7.7 df1.join(df2) - Join on index ---")
df_x = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
df_y = pd.DataFrame({'B': [4, 5, 6]}, index=['a', 'b', 'd'])
result = df_x.join(df_y, how='left')
print("Description: Merge DataFrames using index")
print(result)

# =============================================================================
# 8. RESHAPING DATA
# =============================================================================
print("\n" + "=" * 80)
print("8. RESHAPING DATA")
print("=" * 80)

# 8.1 Pivot
print("\n--- 8.1 df.pivot(index, columns, values) - Reshape data ---")
df_sales = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 150, 120, 160]
})
result = df_sales.pivot(index='date', columns='product', values='sales')
print("Description: Reshape data (rows=index, columns=columns, cells=values)")
print(result)

# 8.2 Pivot table (with aggregation)
print("\n--- 8.2 pd.pivot_table() - Pivot with aggregation ---")
df_data = pd.DataFrame({
    'date': ['2024-01', '2024-01', '2024-02', '2024-02'],
    'product': ['A', 'A', 'B', 'B'],
    'sales': [100, 150, 120, 160]
})
result = pd.pivot_table(df_data, index='date', columns='product', 
                       values='sales', aggfunc='sum', fill_value=0)
print("Description: Pivot with aggregation (handles duplicates)")
print(result)

# 8.3 Melt (unpivot)
print("\n--- 8.3 pd.melt() - Unpivot (wide to long) ---")
df_wide = pd.DataFrame({
    'id': [1, 2],
    'Jan': [100, 200],
    'Feb': [110, 210]
})
result = pd.melt(df_wide, id_vars=['id'], var_name='month', value_name='sales')
print("Description: Convert wide format to long format")
print(result)

# 8.4 Stack and Unstack
print("\n--- 8.4 df.stack() / df.unstack() - Pivot indexes ---")
df_multi = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['row1', 'row2'])
print("Original:")
print(df_multi)
print("\nStacked (pivot column to row):")
print(df_multi.stack())

# 8.5 Transpose
print("\n--- 8.5 df.T or df.transpose() - Swap rows and columns ---")
print("Description: Flip DataFrame (rows ↔ columns)")
print(df_multi.T)

# =============================================================================
# 9. HANDLING MISSING DATA
# =============================================================================
print("\n" + "=" * 80)
print("9. HANDLING MISSING DATA")
print("=" * 80)

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5]
})

# 9.1 Detect missing values
print("\n--- 9.1 df.isna() / df.isnull() - Detect missing values ---")
print("Description: Returns boolean DataFrame (True = missing)")
print(df_missing.isna())

# 9.2 Count missing values
print("\n--- 9.2 df.isna().sum() - Count missing per column ---")
print("Description: Count missing values in each column")
print(df_missing.isna().sum())

# 9.3 Drop rows with missing values
print("\n--- 9.3 df.dropna() - Remove rows with missing values ---")
print("Description: Remove rows containing any NaN")
print(df_missing.dropna())

# 9.4 Drop columns with missing values
print("\n--- 9.4 df.dropna(axis=1) - Remove columns with missing ---")
print("Description: Remove columns containing any NaN")
print(df_missing.dropna(axis=1))

# 9.5 Fill missing values with constant
print("\n--- 9.5 df.fillna(value) - Fill missing with value ---")
print("Description: Replace NaN with specified value")
print(df_missing.fillna(0))

# 9.6 Fill with mean/median
print("\n--- 9.6 df.fillna(df.mean()) - Fill with column mean ---")
print("Description: Replace NaN with column statistics")
print(df_missing.fillna(df_missing.mean()))

# 9.7 Forward fill
print("\n--- 9.7 df.ffill() - Forward fill (propagate last valid) ---")
print("Description: Fill NaN with previous valid value")
print(df_missing.ffill())

# 9.8 Backward fill
print("\n--- 9.8 df.bfill() - Backward fill (propagate next valid) ---")
print("Description: Fill NaN with next valid value")
print(df_missing.bfill())

# 9.9 Interpolate
print("\n--- 9.9 df.interpolate() - Interpolate missing values ---")
print("Description: Fill NaN using interpolation")
print(df_missing.interpolate())

# =============================================================================
# 10. STRING OPERATIONS
# =============================================================================
print("\n" + "=" * 80)
print("10. STRING OPERATIONS (df['col'].str.*)")
print("=" * 80)

df_str = pd.DataFrame({
    'name': ['  Alice  ', 'BOB', 'charlie', 'David'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com']
})

# 10.1 Lower, upper, title case
print("\n--- 10.1 str.lower() / upper() / title() - Change case ---")
print("Original:", df_str['name'].tolist())
print("Lower:", df_str['name'].str.lower().tolist())
print("Upper:", df_str['name'].str.upper().tolist())
print("Title:", df_str['name'].str.title().tolist())

# 10.2 Strip whitespace
print("\n--- 10.2 str.strip() - Remove whitespace ---")
print("Description: Remove leading/trailing whitespace")
print(df_str['name'].str.strip().tolist())

# 10.3 Contains
print("\n--- 10.3 str.contains('pattern') - Check if contains substring ---")
print("Description: Boolean check for substring presence")
print(df_str['email'].str.contains('alice'))

# 10.4 Replace
print("\n--- 10.4 str.replace('old', 'new') - Replace substring ---")
print("Description: Replace substring in all values")
print(df_str['email'].str.replace('@email.com', '@company.com').tolist())

# 10.5 Split
print("\n--- 10.5 str.split('delimiter') - Split string ---")
print("Description: Split strings into lists")
print(df_str['email'].str.split('@'))

# 10.6 Extract with regex
print("\n--- 10.6 str.extract(r'pattern') - Extract with regex ---")
print("Description: Extract pattern using regular expression")
print(df_str['email'].str.extract(r'(.+)@'))

# 10.7 String length
print("\n--- 10.7 str.len() - Get string length ---")
print("Description: Returns length of each string")
print(df_str['name'].str.len())

# 10.8 Startswith, endswith
print("\n--- 10.8 str.startswith() / endswith() - Check prefix/suffix ---")
print("Starts with 'a':", df_str['email'].str.startswith('a').tolist())
print("Ends with '.com':", df_str['email'].str.endswith('.com').tolist())

# =============================================================================
# 11. DATETIME OPERATIONS
# =============================================================================
print("\n" + "=" * 80)
print("11. DATETIME OPERATIONS")
print("=" * 80)

df_dates = pd.DataFrame({
    'date_str': ['2024-01-15', '2024-02-20', '2024-03-25'],
    'sales': [100, 150, 200]
})

# 11.1 Convert to datetime
print("\n--- 11.1 pd.to_datetime() - Convert to datetime ---")
df_dates['date'] = pd.to_datetime(df_dates['date_str'])
print("Description: Convert string to datetime object")
print(df_dates.dtypes)

# 11.2 Extract date components
print("\n--- 11.2 dt.year / month / day - Extract components ---")
df_dates['year'] = df_dates['date'].dt.year
df_dates['month'] = df_dates['date'].dt.month
df_dates['day'] = df_dates['date'].dt.day
df_dates['day_name'] = df_dates['date'].dt.day_name()
print("Description: Extract year, month, day, day name from datetime")
print(df_dates)

# 11.3 Date arithmetic
print("\n--- 11.3 Date arithmetic - Add/subtract time ---")
df_dates['next_week'] = df_dates['date'] + pd.Timedelta(days=7)
df_dates['days_since'] = (pd.Timestamp.now() - df_dates['date']).dt.days
print("Description: Add/subtract time periods")
print(df_dates[['date', 'next_week', 'days_since']])

# 11.4 Resample (time series)
print("\n--- 11.4 df.resample() - Time series resampling ---")
df_ts = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'value': range(10)
})
df_ts.set_index('date', inplace=True)
result = df_ts.resample('3D').sum()  # Group by 3 days
print("Description: Aggregate time series by time period")
print(result)

# =============================================================================
# 12. APPLY FUNCTIONS & LAMBDA
# =============================================================================
print("\n" + "=" * 80)
print("12. APPLY FUNCTIONS & LAMBDA")
print("=" * 80)

df_apply = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [1, 20, 30, 40]
})

# 12.1 Apply to column
print("\n--- 12.1 df['col'].apply(func) - Apply function to column ---")
result = df_apply['A'].apply(lambda x: x ** 2)
print("Description: Apply function to each value in column")
print(result)

# 12.2 Apply to DataFrame
print("\n--- 12.2 df.apply(func) - Apply to each column ---")
result = df_apply.apply(lambda x: x.sum())
print("Description: Apply function to each column (axis=0)")
print(result)

# 12.3 Apply to each row
print("\n--- 12.3 df.apply(func, axis=1) - Apply to each row ---")
result = df_apply.apply(lambda row: row['A'] + row['B'], axis=1)
print("Description: Apply function across columns (row-wise)")
print(result)

# 12.4 applymap (element-wise)
print("\n--- 12.4 df.applymap(func) - Apply to every element ---")
result = df_apply.applymap(lambda x: x * 2)
print("Description: Apply function to every single element")
print(result)

# 12.5 map (for Series)
print("\n--- 12.5 df['col'].map(dict/func) - Map values ---")
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
result = df_apply['A'].map(mapping)
print("Description: Map values using dictionary or function")
print(result)

# 12.6 replace
print("\n--- 12.6 df.replace(old, new) - Replace values ---")
result = df_apply.replace({1: 100, 2: 200})
print("Description: Replace specific values")
print(result)

# =============================================================================
# 13. STATISTICAL OPERATIONS
# =============================================================================
print("\n" + "=" * 80)
print("13. STATISTICAL OPERATIONS")
print("=" * 80)

df_stats = pd.DataFrame({
    'values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

print("\n--- 13.1 Basic statistics ---")
print(f"mean(): {df_stats['values'].mean()} - Average")
print(f"median(): {df_stats['values'].median()} - Middle value")
print(f"mode(): {df_stats['values'].mode().values} - Most frequent")
print(f"std(): {df_stats['values'].std():.2f} - Standard deviation")
print(f"var(): {df_stats['values'].var():.2f} - Variance")
print(f"min(): {df_stats['values'].min()} - Minimum")
print(f"max(): {df_stats['values'].max()} - Maximum")
print(f"sum(): {df_stats['values'].sum()} - Sum of all values")
print(f"count(): {df_stats['values'].count()} - Non-null count")

print("\n--- 13.2 Quantiles and percentiles ---")
print(f"quantile(0.25): {df_stats['values'].quantile(0.25)} - 25th percentile")
print(f"quantile(0.5): {df_stats['values'].quantile(0.5)} - 50th percentile (median)")
print(f"quantile(0.75): {df_stats['values'].quantile(0.75)} - 75th percentile")

print("\n--- 13.3 Correlation and covariance ---")
df_corr = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [5, 4, 3, 2, 1]
})
print("corr() - Correlation matrix:")
print(df_corr.corr())
print("\ncov() - Covariance matrix:")
print(df_corr.cov())

# 13.4 Cumulative operations
print("\n--- 13.4 Cumulative operations ---")
print("cumsum() - Cumulative sum:", df_stats['values'].cumsum().tolist())
print("cumprod() - Cumulative product:", df_apply['A'].cumprod().tolist())
print("cummax() - Cumulative maximum:", df_stats['values'].cummax().tolist())
print("cummin() - Cumulative minimum:", df_stats['values'].cummin().tolist())

# =============================================================================
# 14. DUPLICATE HANDLING
# =============================================================================
print("\n" + "=" * 80)
print("14. DUPLICATE HANDLING")
print("=" * 80)

df_dup = pd.DataFrame({
    'A': [1, 1, 2, 2, 3],
    'B': ['a', 'a', 'b', 'c', 'c']
})

# 14.1 Detect duplicates
print("\n--- 14.1 df.duplicated() - Detect duplicate rows ---")
print("Description: Returns boolean Series (True = duplicate)")
print(df_dup.duplicated())

# 14.2 Drop duplicates
print("\n--- 14.2 df.drop_duplicates() - Remove duplicates ---")
print("Description: Keep first occurrence, remove rest")
print(df_dup.drop_duplicates())

# 14.3 Drop duplicates based on specific columns
print("\n--- 14.3 df.drop_duplicates(subset=['col']) - Remove based on column ---")
print("Description: Remove duplicates based on specific column(s)")
print(df_dup.drop_duplicates(subset=['A']))

# 14.4 Keep last duplicate
print("\n--- 14.4 df.drop_duplicates(keep='last') - Keep last occurrence ---")
print("Description: Keep last occurrence instead of first")
print(df_dup.drop_duplicates(keep='last'))

# =============================================================================
# 15. ADVANCED INDEXING
# =============================================================================
print("\n" + "=" * 80)
print("15. ADVANCED INDEXING")
print("=" * 80)

# 15.1 Set index
print("\n--- 15.1 df.set_index('col') - Set column as index ---")
df_temp = df.set_index('name')
print("Description: Use column as row labels")
print(df_temp.head(3))

# 15.2 Reset index
print("\n--- 15.2 df.reset_index() - Reset index to default ---")
print("Description: Convert index back to column")
print(df_temp.reset_index().head(3))

# 15.3 MultiIndex
print("\n--- 15.3 MultiIndex - Hierarchical indexing ---")
df_multi = pd.DataFrame({
    'dept': ['IT', 'IT', 'HR', 'HR'],
    'level': ['Junior', 'Senior', 'Junior', 'Senior'],
    'salary': [50000, 80000, 45000, 70000]
})
df_multi = df_multi.set_index(['dept', 'level'])
print("Description: Multiple levels of row indexes")
print(df_multi)

# =============================================================================
# 16. CATEGORICAL DATA
# =============================================================================
print("\n" + "=" * 80)
print("16. CATEGORICAL DATA")
print("=" * 80)

# 16.1 Convert to category
print("\n--- 16.1 df['col'].astype('category') - Convert to categorical ---")
df_cat = df.copy()
df_cat['department'] = df_cat['department'].astype('category')
print("Description: Reduce memory for repeated values")
print(df_cat['department'].dtype)
print(f"Categories: {df_cat['department'].cat.categories.tolist()}")

# 16.2 Get dummies (one-hot encoding)
print("\n--- 16.2 pd.get_dummies() - One-hot encoding ---")
result = pd.get_dummies(df['department'], prefix='dept')
print("Description: Convert categorical to binary columns")
print(result)

# =============================================================================
# 17. WINDOW FUNCTIONS
# =============================================================================
print("\n" + "=" * 80)
print("17. WINDOW FUNCTIONS (Rolling, Expanding)")
print("=" * 80)

df_window = pd.DataFrame({
    'values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

# 17.1 Rolling window
print("\n--- 17.1 df.rolling(window=n) - Moving window calculations ---")
df_window['rolling_mean_3'] = df_window['values'].rolling(window=3).mean()
print("Description: Calculate statistics over sliding window")
print(df_window)

# 17.2 Expanding window
print("\n--- 17.2 df.expanding() - Cumulative window ---")
df_window['expanding_mean'] = df_window['values'].expanding().mean()
print("Description: Calculate statistics from start to current row")
print(df_window[['values', 'expanding_mean']])

# 17.3 Shift
print("\n--- 17.3 df.shift(n) - Shift values by n periods ---")
df_window['shifted_1'] = df_window['values'].shift(1)
df_window['shifted_minus1'] = df_window['values'].shift(-1)
print("Description: Move values up/down (positive=down, negative=up)")
print(df_window[['values', 'shifted_1', 'shifted_minus1']].head())

# 17.4 Diff
print("\n--- 17.4 df.diff() - Calculate difference between rows ---")
df_window['diff'] = df_window['values'].diff()
print("Description: Current row minus previous row")
print(df_window[['values', 'diff']].head())

# 17.5 Pct_change
print("\n--- 17.5 df.pct_change() - Percentage change ---")
df_window['pct_change'] = df_window['values'].pct_change()
print("Description: Percentage change from previous row")
print(df_window[['values', 'pct_change']].head())

# =============================================================================
# 18. PERFORMANCE & OPTIMIZATION
# =============================================================================
print("\n" + "=" * 80)
print("18. PERFORMANCE & OPTIMIZATION")
print("=" * 80)

# 18.1 Memory usage
print("\n--- 18.1 df.memory_usage() - Check memory consumption ---")
print("Description: Memory used by each column")
print(df.memory_usage(deep=True))

# 18.2 Optimize dtypes
print("\n--- 18.2 Optimize data types to reduce memory ---")
df_opt = df.copy()
print(f"Before: {df_opt.memory_usage(deep=True).sum()} bytes")
df_opt['id'] = df_opt['id'].astype('int8')  # Small integers
df_opt['department'] = df_opt['department'].astype('category')  # Repeated strings
print(f"After: {df_opt.memory_usage(deep=True).sum()} bytes")
print("Description: Use smaller dtypes and categories for efficiency")

# 18.3 Query vs boolean indexing (faster)
print("\n--- 18.3 Use .query() for faster filtering ---")
print("Description: query() is often faster than boolean indexing")
print("df.query('age > 30') is faster than df[df['age'] > 30]")

# 18.4 Use vectorized operations
print("\n--- 18.4 Vectorized operations vs loops ---")
print("Description: ALWAYS use vectorized operations, avoid loops")
print("GOOD: df['new'] = df['A'] + df['B']")
print("BAD: for i in range(len(df)): df.loc[i, 'new'] = df.loc[i, 'A'] + df.loc[i, 'B']")

# =============================================================================
# 19. INPUT/OUTPUT OPERATIONS
# =============================================================================
print("\n" + "=" * 80)
print("19. INPUT/OUTPUT OPERATIONS")
print("=" * 80)

print("\n--- 19.1 File reading ---")
print("pd.read_csv('file.csv') - Read CSV")
print("pd.read_excel('file.xlsx') - Read Excel")
print("pd.read_json('file.json') - Read JSON")
print("pd.read_sql('SELECT * FROM table', connection) - Read from SQL")
print("pd.read_html('url') - Read HTML tables")
print("pd.read_parquet('file.parquet') - Read Parquet")

print("\n--- 19.2 File writing ---")
print("df.to_csv('file.csv', index=False) - Write to CSV")
print("df.to_excel('file.xlsx', index=False) - Write to Excel")
print("df.to_json('file.json') - Write to JSON")
print("df.to_sql('table_name', connection) - Write to SQL")
print("df.to_html('file.html') - Write to HTML")
print("df.to_parquet('file.parquet') - Write to Parquet (efficient)")

print("\n--- 19.3 Clipboard ---")
print("df.to_clipboard() - Copy to clipboard")
print("pd.read_clipboard() - Read from clipboard")

# =============================================================================
# 20. USEFUL TRICKS & PATTERNS
# =============================================================================
print("\n" + "=" * 80)
print("20. USEFUL TRICKS & PATTERNS")
print("=" * 80)

# 20.1 Sample data
print("\n--- 20.1 df.sample(n) - Get random sample ---")
print("Description: Get random rows (useful for testing)")
print(df.sample(n=3))

# 20.2 Nlargest / Nsmallest
print("\n--- 20.2 df.nlargest(n, 'col') / nsmallest() ---")
print("Description: Get top/bottom N rows by column value")
print(df.nlargest(3, 'salary')[['name', 'salary']])

# 20.3 Where / Mask
print("\n--- 20.3 df.where(condition, other) - Conditional replacement ---")
result = df['age'].where(df['age'] > 30, 'Young')
print("Description: Keep values where condition is True, else replace")
print(result)

# 20.4 Clip
print("\n--- 20.4 df.clip(lower, upper) - Limit values to range ---")
result = df['age'].clip(lower=28, upper=32)
print("Description: Cap values at lower/upper bounds")
print(result.tolist())

# 20.5 Rank
print("\n--- 20.5 df['col'].rank() - Assign ranks ---")
df_temp = df.copy()
df_temp['salary_rank'] = df_temp['salary'].rank(ascending=False)
print("Description: Rank values (1=highest with ascending=False)")
print(df_temp[['name', 'salary', 'salary_rank']])

# 20.6 Between
print("\n--- 20.6 df['col'].between(low, high) - Check if in range ---")
result = df[df['age'].between(28, 32)]
print("Description: Filter values within range (inclusive)")
print(result[['name', 'age']])

# 20.7 Explode (expand lists)
print("\n--- 20.7 df.explode('col') - Expand list column to rows ---")
df_lists = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'scores': [[90, 85, 88], [75, 80]]
})
result = df_lists.explode('scores')
print("Description: Convert each list element to separate row")
print(result)

# 20.8 Crosstab
print("\n--- 20.8 pd.crosstab() - Cross-tabulation ---")
df_cross = pd.DataFrame({
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'dept': ['IT', 'IT', 'HR', 'HR', 'IT']
})
result = pd.crosstab(df_cross['gender'], df_cross['dept'])
print("Description: Count occurrences of combinations")
print(result)

# 20.9 Cut (bin continuous data)
print("\n--- 20.9 pd.cut() - Bin continuous values ---")
df_temp = df.copy()
df_temp['age_group'] = pd.cut(df_temp['age'], bins=[0, 30, 40, 100], 
                               labels=['Young', 'Middle', 'Senior'])
print("Description: Convert continuous to categorical bins")
print(df_temp[['name', 'age', 'age_group']])

# 20.10 QCut (quantile-based bins)
print("\n--- 20.10 pd.qcut() - Quantile-based binning ---")
df_temp['salary_quartile'] = pd.qcut(df_temp['salary'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print("Description: Bin into equal-sized buckets")
print(df_temp[['name', 'salary', 'salary_quartile']])

print("\n" + "=" * 80)
print("END OF PANDAS COMPLETE GUIDE")
print("=" * 80)
print("\n📚 Topics Covered:")
print("1. Data Creation  2. Viewing Data  3. Selection  4. Modification")
print("5. Sorting  6. Grouping  7. Merging  8. Reshaping  9. Missing Data")
print("10. Strings  11. Datetime  12. Apply  13. Statistics  14. Duplicates")
print("15. Indexing  16. Categorical  17. Windows  18. Performance")
print("19. I/O Operations  20. Useful Tricks")
print("\n✅ You're ready for pandas interviews!")


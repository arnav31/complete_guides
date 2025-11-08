"""
PANDAS QUICK REFERENCE CHEATSHEET
One-line summary of most important functions
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("PANDAS QUICK REFERENCE - Most Important Functions")
print("=" * 80)

# Sample DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 70000],
    'dept': ['IT', 'HR', 'IT', 'Finance', 'HR']
})

print("\n📋 ESSENTIAL PANDAS COMMANDS (Top 50)\n")

commands = [
    # Data Creation & Loading
    ("DATA CREATION", [
        "pd.DataFrame(dict) - Create from dictionary",
        "pd.Series(list) - Create Series",
        "pd.read_csv('file.csv') - Read CSV",
        "pd.read_excel('file.xlsx') - Read Excel",
        "pd.read_json('file.json') - Read JSON",
    ]),
    
    # Viewing Data
    ("VIEWING DATA", [
        "df.head(n) - First n rows",
        "df.tail(n) - Last n rows",
        "df.info() - Schema & types",
        "df.describe() - Stats summary",
        "df.shape - (rows, cols)",
        "df.columns - Column names",
        "df.dtypes - Column types",
    ]),
    
    # Selection
    ("SELECTION", [
        "df['col'] - Select column (Series)",
        "df[['col1','col2']] - Select columns (DataFrame)",
        "df.loc[row, col] - Label-based",
        "df.iloc[row, col] - Position-based",
        "df.at[row, col] - Fast single value (label)",
        "df.iat[row, col] - Fast single value (position)",
        "df[df['col'] > value] - Boolean filter",
        "df.query('col > value') - SQL-style filter",
    ]),
    
    # Modification
    ("MODIFICATION", [
        "df['new_col'] = values - Add column",
        "df.drop(columns=[...]) - Remove columns",
        "df.drop(index=[...]) - Remove rows",
        "df.rename(columns={...}) - Rename columns",
        "df.insert(loc, 'col', values) - Insert at position",
    ]),
    
    # Sorting
    ("SORTING", [
        "df.sort_values('col') - Sort by column",
        "df.sort_values(['c1','c2']) - Sort by multiple",
        "df.sort_index() - Sort by index",
    ]),
    
    # Aggregation
    ("AGGREGATION", [
        "df.groupby('col').agg('mean') - Group & aggregate",
        "df.groupby('col').agg(['mean','sum']) - Multiple agg",
        "df.groupby(['c1','c2'])['col'].mean() - Multi-column group",
        "df['col'].value_counts() - Count unique values",
        "df['col'].unique() - Get unique values",
        "df['col'].nunique() - Count unique",
    ]),
    
    # Merging
    ("MERGING", [
        "pd.merge(df1, df2, on='key') - Inner join",
        "pd.merge(df1, df2, how='left') - Left join",
        "pd.merge(df1, df2, how='right') - Right join",
        "pd.merge(df1, df2, how='outer') - Full join",
        "pd.concat([df1, df2], axis=0) - Stack vertical",
        "pd.concat([df1, df2], axis=1) - Stack horizontal",
    ]),
    
    # Missing Data
    ("MISSING DATA", [
        "df.isna() - Detect NaN",
        "df.dropna() - Remove NaN rows",
        "df.fillna(value) - Fill NaN",
        "df.ffill() - Forward fill",
        "df.bfill() - Backward fill",
        "df.interpolate() - Interpolate NaN",
    ]),
    
    # String Operations
    ("STRING OPS", [
        "df['col'].str.lower() - Lowercase",
        "df['col'].str.upper() - Uppercase",
        "df['col'].str.strip() - Remove whitespace",
        "df['col'].str.contains('text') - Check contains",
        "df['col'].str.replace('old', 'new') - Replace",
        "df['col'].str.split('delim') - Split string",
    ]),
    
    # DateTime
    ("DATETIME", [
        "pd.to_datetime(df['col']) - Convert to datetime",
        "df['date'].dt.year - Extract year",
        "df['date'].dt.month - Extract month",
        "df['date'].dt.day_name() - Get day name",
    ]),
    
    # Apply Functions
    ("APPLY", [
        "df['col'].apply(func) - Apply to column",
        "df.apply(func, axis=1) - Apply to rows",
        "df['col'].map(dict) - Map values",
    ]),
    
    # Statistics
    ("STATISTICS", [
        "df['col'].mean() - Average",
        "df['col'].median() - Median",
        "df['col'].std() - Standard deviation",
        "df['col'].min() / .max() - Min/Max",
        "df['col'].sum() - Sum",
        "df['col'].count() - Count non-null",
        "df.corr() - Correlation matrix",
    ]),
    
    # Duplicates
    ("DUPLICATES", [
        "df.duplicated() - Detect duplicates",
        "df.drop_duplicates() - Remove duplicates",
    ]),
    
    # Reshaping
    ("RESHAPING", [
        "df.pivot(index, columns, values) - Pivot",
        "pd.pivot_table(df, ...) - Pivot with agg",
        "pd.melt(df, id_vars) - Unpivot",
        "df.T - Transpose",
    ]),
    
    # Export
    ("EXPORT", [
        "df.to_csv('file.csv', index=False) - Save CSV",
        "df.to_excel('file.xlsx', index=False) - Save Excel",
        "df.to_json('file.json') - Save JSON",
    ]),
    
    # Useful Tricks
    ("USEFUL TRICKS", [
        "df.sample(n) - Random sample",
        "df.nlargest(n, 'col') - Top N values",
        "df.nsmallest(n, 'col') - Bottom N values",
        "pd.get_dummies(df['col']) - One-hot encoding",
        "df['col'].between(low, high) - Range filter",
        "df['col'].rank() - Rank values",
        "pd.cut(df['col'], bins) - Bin continuous",
        "df.rolling(window=n).mean() - Moving average",
    ]),
]

for category, items in commands:
    print(f"\n{category}:")
    print("-" * 80)
    for item in items:
        print(f"  • {item}")

print("\n" + "=" * 80)
print("INTERVIEW TIP: Practice these 50+ functions and you're ready!")
print("=" * 80)

# Show live examples of most commonly asked interview questions
print("\n\n🎯 TOP 10 INTERVIEW QUESTIONS WITH LIVE EXAMPLES\n")
print("=" * 80)

print("\n1️⃣  Filter rows where salary > 60000")
print(df[df['salary'] > 60000][['name', 'salary']])

print("\n2️⃣  Group by department and get average salary")
print(df.groupby('dept')['salary'].mean())

print("\n3️⃣  Add a new column (bonus = 10% of salary)")
df['bonus'] = df['salary'] * 0.10
print(df[['name', 'salary', 'bonus']].head())

print("\n4️⃣  Sort by salary (descending)")
print(df.sort_values('salary', ascending=False)[['name', 'salary']].head())

print("\n5️⃣  Get top 3 highest salaries")
print(df.nlargest(3, 'salary')[['name', 'salary']])

print("\n6️⃣  Count employees per department")
print(df['dept'].value_counts())

print("\n7️⃣  Find employees in IT or HR department")
print(df[df['dept'].isin(['IT', 'HR'])][['name', 'dept']])

print("\n8️⃣  Get employees aged between 28 and 32")
print(df[df['age'].between(28, 32)][['name', 'age']])

print("\n9️⃣  Create age groups (Young, Middle, Senior)")
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 35, 100], 
                         labels=['Young', 'Middle', 'Senior'])
print(df[['name', 'age', 'age_group']])

print("\n🔟 Pivot: Show count of employees by dept")
pivot_df = pd.crosstab(df['dept'], 'count')
print(pivot_df)

print("\n" + "=" * 80)
print("✅ Master these patterns and ace your pandas interview!")
print("=" * 80)


# 🐼 Pandas Interview Preparation Guide

Complete pandas learning resources from basic to advanced - Everything you need to ace data science interviews!

## 📁 Files in this Directory

### 1. **`pandas_complete_guide.py`** ⭐ MAIN RESOURCE
**The most comprehensive pandas tutorial (1000+ lines)**

Covers 20 major topics:
- ✅ Data Creation & Loading
- ✅ Viewing & Inspecting Data
- ✅ Selection & Indexing (loc, iloc, at, iat, boolean)
- ✅ Adding, Modifying, Deleting Columns/Rows
- ✅ Sorting
- ✅ Grouping & Aggregation
- ✅ Merging, Joining, Concatenating
- ✅ Reshaping Data (pivot, melt, stack, unstack)
- ✅ Handling Missing Data
- ✅ String Operations
- ✅ DateTime Operations
- ✅ Apply Functions & Lambda
- ✅ Statistical Operations
- ✅ Duplicate Handling
- ✅ Advanced Indexing
- ✅ Categorical Data
- ✅ Window Functions (rolling, expanding, shift)
- ✅ Performance & Optimization
- ✅ Input/Output Operations
- ✅ Useful Tricks & Patterns

**Each function includes:**
- 📝 Description
- 💻 Working example
- 📊 Output
- 💡 Best practices

**Run it:**
```bash
python pandas_complete_guide.py
```

---

### 2. **`pandas_quick_reference.py`** 🚀 CHEATSHEET
**Quick lookup guide with 50+ essential functions**

Perfect for:
- Quick revision before interviews
- Command reference while coding
- Top 10 interview questions with live examples

**Run it:**
```bash
python pandas_quick_reference.py
```

---

### 3. **`pandas_functions_pretty.py`** 🎨 PRETTY DISPLAY
**Beautiful console output using the Rich library**

Shows how to display pandas DataFrames with:
- Colorful borders
- Emoji icons
- Professional formatting
- Clean tables

**Run it:**
```bash
python pandas_functions_pretty.py
```

---

### 4. **`pretty_display_examples.py`** 🌈 FORMATTING OPTIONS
**7 different methods to format pandas output**

Demonstrates:
- Standard pandas configuration
- Tabulate library
- Rich library (beautiful tables)
- DataFrame.to_string()
- DataFrame.to_markdown()
- Styled DataFrames
- PrettyTable

**Run it:**
```bash
python pretty_display_examples.py
```

---

### 5. **`pandas_functions.py`** 📚 YOUR PRACTICE FILE
**Your working file with basic examples**

Use this to:
- Practice concepts
- Add your own examples
- Experiment with code

---

## 🚀 Getting Started

### 1. Activate Virtual Environment
```bash
source /Users/arnavgupta/Arnav_projects/.venv/bin/activate
```

### 2. Install Required Packages (if needed)
```bash
pip install pandas numpy openpyxl rich tabulate prettytable
```

### 3. Start Learning!

**For Complete Learning:**
```bash
python pandas_complete_guide.py | less
```
(Press `space` to scroll, `q` to quit)

**For Quick Revision:**
```bash
python pandas_quick_reference.py
```

---

## 📖 Learning Path

### Beginner (Week 1)
Focus on sections 1-5 of `pandas_complete_guide.py`:
- Data Creation
- Viewing Data
- Selection & Indexing
- Basic Modifications
- Sorting

### Intermediate (Week 2)
Focus on sections 6-12:
- Grouping & Aggregation
- Merging & Joining
- Reshaping
- Missing Data
- String Operations
- DateTime
- Apply Functions

### Advanced (Week 3)
Focus on sections 13-20:
- Statistics
- Duplicates
- Advanced Indexing
- Categorical Data
- Window Functions
- Performance Optimization
- I/O Operations
- Advanced Tricks

---

## 🎯 Interview Preparation Tips

### 1. **Master the Top 20 Functions**
```python
# These appear in 80% of interviews:
df.head(), df.tail(), df.info(), df.describe()
df.loc[], df.iloc[], df[condition]
df.groupby().agg()
pd.merge(), pd.concat()
df.fillna(), df.dropna()
df.apply(), df['col'].map()
df.sort_values(), df.drop_duplicates()
df['col'].value_counts()
pd.pivot_table(), pd.melt()
```

### 2. **Common Interview Questions**
- ✅ How to filter rows based on conditions?
- ✅ How to handle missing data?
- ✅ How to group data and calculate aggregates?
- ✅ How to merge/join DataFrames?
- ✅ How to reshape data (wide to long, long to wide)?
- ✅ How to apply custom functions?
- ✅ How to work with datetime data?
- ✅ How to optimize performance?

### 3. **Practice These Patterns**
```python
# Pattern 1: Filter and Transform
df[df['age'] > 30]['salary'].mean()

# Pattern 2: GroupBy + Agg
df.groupby('dept').agg({'salary': 'mean', 'age': ['min', 'max']})

# Pattern 3: Chain Operations
(df[df['salary'] > 50000]
   .groupby('dept')['salary']
   .mean()
   .sort_values(ascending=False))

# Pattern 4: Apply with Lambda
df['salary_bracket'] = df['salary'].apply(
    lambda x: 'High' if x > 60000 else 'Low'
)

# Pattern 5: Multiple Conditions
df[(df['age'] > 25) & (df['dept'].isin(['IT', 'HR']))]
```

---

## 💡 Pro Tips

### Performance Optimization
```python
# Use vectorized operations (FAST)
df['new'] = df['a'] + df['b']

# Avoid loops (SLOW)
for i in range(len(df)):
    df.loc[i, 'new'] = df.loc[i, 'a'] + df.loc[i, 'b']

# Use categories for repeated strings
df['dept'] = df['dept'].astype('category')

# Use query for complex filters
df.query("age > 30 and salary > 50000")
```

### Memory Optimization
```python
# Check memory usage
df.memory_usage(deep=True)

# Optimize dtypes
df['id'] = df['id'].astype('int32')  # Instead of int64
df['category'] = df['category'].astype('category')  # For repeated strings
```

---

## 🛠️ Useful Resources

- **Official Docs:** https://pandas.pydata.org/docs/
- **10 Minutes to Pandas:** https://pandas.pydata.org/docs/user_guide/10min.html
- **Pandas Exercises:** https://github.com/guipsamora/pandas_exercises

---

## 📝 Practice Exercises

After studying the guide, try these:

1. Load a CSV file and find the top 5 highest values in a column
2. Group by category and calculate mean, median, and count
3. Merge two DataFrames on a common key
4. Handle missing values using multiple strategies
5. Reshape data from wide to long format
6. Create a pivot table with multiple aggregations
7. Apply a custom function to clean string data
8. Extract year, month, day from datetime column
9. Calculate rolling average over a window
10. Optimize a DataFrame to reduce memory usage

---

## 🎓 Certification Ready

After mastering these files, you'll be ready for:
- Data Analyst interviews
- Data Scientist interviews
- Business Analyst interviews
- Python Developer (Data) interviews
- Pandas certification exams

---

## 📞 Quick Reference Card

```python
# CREATING
df = pd.DataFrame(dict)
df = pd.read_csv('file.csv')

# VIEWING
df.head() | df.tail() | df.info() | df.describe()

# SELECTING
df['col'] | df[['c1','c2']] | df.loc[] | df.iloc[]

# FILTERING
df[df['col'] > value] | df.query('col > 5')

# SORTING
df.sort_values('col', ascending=False)

# GROUPING
df.groupby('col').agg('mean')

# MERGING
pd.merge(df1, df2, on='key', how='left')

# MISSING
df.fillna(0) | df.dropna() | df.isna()

# APPLYING
df['col'].apply(func) | df.apply(func, axis=1)

# EXPORTING
df.to_csv('out.csv', index=False)
```

---

## ✅ Checklist for Interview Readiness

- [ ] Understand all 20 sections in `pandas_complete_guide.py`
- [ ] Can write code for top 10 interview questions without looking
- [ ] Know difference between loc, iloc, at, iat
- [ ] Understand inner, left, right, outer joins
- [ ] Can handle missing data with 3+ strategies
- [ ] Know how to group and aggregate data
- [ ] Can reshape data (pivot, melt)
- [ ] Understand apply, map, applymap differences
- [ ] Know datetime operations
- [ ] Can optimize DataFrame memory usage

---

## 🏆 Good Luck with Your Interviews!

Practice daily, understand concepts deeply, and you'll ace any pandas interview! 🚀

**Remember:** It's not about memorizing syntax, it's about understanding patterns and solving problems efficiently.


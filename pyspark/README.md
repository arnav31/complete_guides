# 🔥 PySpark Interview Preparation Guide

Complete PySpark learning resources from basic to advanced - Everything you need to ace Big Data interviews!

## 📁 Files in this Directory

### 1. **pyspark_complete_guide.py** (35KB) ⭐⭐⭐⭐⭐
**THE ULTIMATE PYSPARK GUIDE**

**Covers 14 major topics:**
1. DataFrame Creation (4 methods)
2. Reading & Writing Data (CSV, Parquet, JSON)
3. Basic Transformations (select, filter, withColumn, drop, etc.)
4. Aggregations (groupBy, agg, count, sum, avg)
5. Joins (6 types: inner, left, right, outer, semi, anti)
6. Column Functions (String, Numeric, Conditional)
7. Date & Time Functions (15+ functions)
8. Window Functions (row_number, rank, lag, lead, running total)
9. User Defined Functions (UDF, pandas_udf)
10. SQL Operations (temp views, SQL queries)
11. Null Handling (isNull, dropna, fillna)
12. Performance Optimization (cache, repartition, broadcast)
13. Actions (show, collect, count, take)
14. Common Interview Problems (14+ solved problems)

**Run it:** `python pyspark_complete_guide.py`

### 2. **pyspark_quick_reference.py** (10KB) 🚀
**Quick lookup guide with essential functions**

**Features:**
- All essential PySpark functions in tables
- Column functions reference
- SQL operations
- Join types
- Window functions examples
- UDF examples
- Interview tips
- Common mistakes

**Run it:** `python pyspark_quick_reference.py`

### 3. **pyspark_examples.py** (8KB) 💼
**Your practice file with 30+ examples**

**Organized sections:**
- Basic operations
- Aggregations
- Joins
- String functions
- Date functions
- Conditional logic
- Window functions
- Null handling
- SQL operations
- Performance
- Interview problems

**Run it:** `python pyspark_examples.py`

## 🚀 Quick Start

```bash
# Activate virtual environment
source /Users/arnavgupta/Arnav_projects/.venv/bin/activate

# Install dependencies
cd /Users/arnavgupta/Arnav_projects/padai/pyspark
pip install -r requirements.txt

# Run guides
python pyspark_complete_guide.py      # Complete learning
python pyspark_quick_reference.py     # Quick revision
python pyspark_examples.py            # Practice
```

## 📖 Learning Path

**Week 1:** DataFrames, Transformations, Aggregations  
**Week 2:** Joins, Window Functions, SQL  
**Week 3:** UDFs, Performance, Interview Problems  

## 🎯 Interview Preparation

### Top 20 Must-Know Functions:
```python
# DataFrames
spark.read.csv(), spark.createDataFrame()
df.show(), df.printSchema(), df.count()

# Transformations
df.select(), df.filter(), df.withColumn()
df.groupBy().agg(), df.orderBy()

# Joins
df1.join(df2, condition, join_type)

# Window Functions
row_number().over(windowSpec)
rank(), dense_rank(), lag(), lead()

# SQL
df.createOrReplaceTempView(), spark.sql()

# Performance
df.cache(), df.repartition(), broadcast()
```

### Common Interview Questions:
1. ✅ How to read and write data in PySpark?
2. ✅ What's the difference between transformation and action?
3. ✅ How to handle null values?
4. ✅ How to perform joins?
5. ✅ What are window functions?
6. ✅ How to optimize PySpark jobs?
7. ✅ Difference between UDF and pandas_udf?
8. ✅ How to use SQL with DataFrames?

## 💡 Key Concepts

### Transformations (Lazy):
- `select()`, `filter()`, `withColumn()`, `groupBy()`
- Not executed immediately
- Build execution plan

### Actions (Trigger Computation):
- `show()`, `collect()`, `count()`, `take()`
- Trigger actual computation
- Return results

### Performance Tips:
```python
# Cache frequently used DataFrames
df.cache()

# Use broadcast for small tables
broadcast(small_df)

# Avoid collect() on large data
df.take(10)  # Instead of df.collect()

# Repartition wisely
df.repartition(200)  # Increase parallelism
```

## 🏆 Interview Readiness Checklist

- [ ] Understand DataFrames and RDDs
- [ ] Know all basic transformations
- [ ] Master groupBy and aggregations
- [ ] Understand all join types
- [ ] Can use window functions
- [ ] Know SQL operations
- [ ] Understand lazy evaluation
- [ ] Can handle null values
- [ ] Know performance optimization
- [ ] Can write UDFs
- [ ] Understand partitioning
- [ ] Know broadcast joins

## 🔥 PySpark vs Pandas

| Feature | Pandas | PySpark |
|---------|--------|---------|
| **Data Size** | Small (fits in memory) | Big Data (distributed) |
| **Processing** | Single machine | Cluster |
| **Speed** | Fast for small data | Fast for big data |
| **API** | DataFrame | DataFrame + RDD |
| **SQL** | Limited | Full SQL support |

## ✅ Best Practices

```python
# 1. Always stop Spark when done
spark.stop()

# 2. Use broadcast for small tables
df1.join(broadcast(df2), "id")

# 3. Cache reused DataFrames
df_cached = df.cache()

# 4. Avoid UDFs when possible (use built-in)
# BAD: udf(lambda x: x.upper())
# GOOD: upper(col("name"))

# 5. Use coalesce to reduce partitions
df.coalesce(1).write.csv("output")

# 6. Check execution plan
df.explain()
```

## 🎓 Good Luck!

Master PySpark and ace your Big Data interviews! 🚀

**Remember:** Practice with real datasets and understand the distributed computing concepts!

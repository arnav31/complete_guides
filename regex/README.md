

# 🔍 Regex Interview Preparation Guide

Complete regex (regular expressions) learning resources from basic to advanced - Everything you need to ace technical interviews!

## 📁 Files in this Directory

### 1. **`regex_complete_guide.py`** ⭐ MAIN RESOURCE
**The most comprehensive regex tutorial**

Covers 10 major topics:
- ✅ Basic Patterns (literals, dot, anchors, OR)
- ✅ Character Classes (\d, \w, \s, [abc], ranges)
- ✅ Quantifiers (*, +, ?, {n}, {n,m}, greedy vs non-greedy)
- ✅ Groups and Capturing ((), (?:), (?P<name>), backreferences)
- ✅ Lookahead and Lookbehind (zero-width assertions)
- ✅ Regex Methods (search, match, findall, sub, split)
- ✅ Flags (IGNORECASE, MULTILINE, DOTALL, VERBOSE)
- ✅ Real-World Patterns (email, phone, URL, IP, dates)
- ✅ Advanced Techniques (functions, complex transformations)
- ✅ Common Interview Problems (50+ examples)

**Each pattern includes:**
- 📝 Description
- 💻 Working example
- 📊 Output with Rich formatting
- 💡 Use cases

**Run it:**
```bash
python regex_complete_guide.py
```

---

### 2. **`regex_quick_reference.py`** 🚀 CHEATSHEET
**Quick lookup guide with essential patterns**

Perfect for:
- Quick revision before interviews
- Pattern reference while coding
- Top 10 live examples
- Common mistakes to avoid

**Run it:**
```bash
python regex_quick_reference.py
```

---

### 3. **`regex_examples.py`** 💼 YOUR WORKING FILE
**Practice file with common use cases**

Organized sections:
- Basic patterns
- Validation (email, phone, URL)
- Extraction (hashtags, dates, emails)
- Transformation (HTML cleanup, masking)
- Advanced (log parsing, name extraction)
- Practical applications

**Run it:**
```bash
python regex_examples.py
```

---

## 🚀 Getting Started

### 1. Activate Virtual Environment
```bash
source /Users/arnavgupta/Arnav_projects/.venv/bin/activate
```

### 2. Install Required Packages
```bash
pip install rich
```

### 3. Start Learning!

**For Complete Learning:**
```bash
python regex_complete_guide.py
```

**For Quick Revision:**
```bash
python regex_quick_reference.py
```

**For Practice:**
```bash
python regex_examples.py
```

---

## 📖 Learning Path

### Day 1-2 (Basics)
- Basic patterns (., ^, $, |)
- Character classes (\d, \w, \s, [abc])
- Simple quantifiers (*, +, ?)

### Day 3-4 (Intermediate)
- Complex quantifiers ({n}, {n,m})
- Groups and capturing
- Regex methods (search, findall, sub)

### Day 5-7 (Advanced)
- Lookahead and lookbehind
- Flags and modifiers
- Real-world patterns
- Common interview problems

---

## 🎯 Interview Preparation Tips

### 1. **Master the Core Patterns**
```python
# Most common in interviews:
\d+         # digits
\w+         # words
\s+         # whitespace
[a-z]+      # lowercase letters
.*          # anything (greedy)
.*?         # anything (non-greedy)
^...$       # full string match
(...) # capture group
```

### 2. **Common Interview Questions**
- ✅ How to validate email addresses?
- ✅ How to extract phone numbers?
- ✅ How to remove HTML tags?
- ✅ How to find repeated words?
- ✅ Difference between * and +?
- ✅ What are lookahead assertions?
- ✅ How to use capture groups?
- ✅ When to use re.match() vs re.search()?

### 3. **Practice These Patterns**
```python
# Pattern 1: Email validation
r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Pattern 2: Phone number (US)
r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'

# Pattern 3: Extract hashtags
r'#\w+'

# Pattern 4: Remove HTML
r'<[^>]+>'

# Pattern 5: Find repeated words
r'\b(\w+)\s+\1\b'
```

---

## 💡 Pro Tips

### Always Use Raw Strings
```python
# GOOD
pattern = r'\d+'

# BAD (requires double escaping)
pattern = '\\d+'
```

### Test Multiple Cases
```python
# Always test with:
# - Valid cases
# - Invalid cases
# - Edge cases
# - Empty strings
```

### Understand Greedy vs Non-Greedy
```python
text = "<div>Hello</div><div>World</div>"

# Greedy (matches longest)
r'<div>.*</div>'  # Matches entire string

# Non-greedy (matches shortest)
r'<div>.*?</div>'  # Matches each div separately
```

### Use re.compile() for Performance
```python
# When reusing patterns
pattern = re.compile(r'\d+')
results = pattern.findall(text)
```

---

## 🛠️ Quick Reference Card

```python
# BASIC
.       # Any character
^       # Start of string
$       # End of string
|       # OR operator

# CHARACTER CLASSES
\d      # Digit [0-9]
\w      # Word [a-zA-Z0-9_]
\s      # Whitespace
[abc]   # Any of a, b, c
[^abc]  # Not a, b, or c
[a-z]   # Range

# QUANTIFIERS
*       # 0 or more
+       # 1 or more
?       # 0 or 1
{n}     # Exactly n
{n,m}   # Between n and m

# GROUPS
(...)   # Capture group
(?:...) # Non-capturing
(?P<name>...) # Named group
\1, \2  # Backreference

# ANCHORS
\b      # Word boundary
^       # Line start (with MULTILINE)
$       # Line end (with MULTILINE)

# METHODS
re.search()   # Find first
re.match()    # Match start
re.findall()  # Find all
re.sub()      # Replace
re.split()    # Split
```

---

## 📝 Common Mistakes to Avoid

### 1. Forgetting Raw Strings
```python
# ✗ WRONG
pattern = "\d+"

# ✓ CORRECT
pattern = r"\d+"
```

### 2. Not Escaping Special Characters
```python
# To match a literal dot
r"\."  # ✓ Correct
r"."   # ✗ Wrong (matches any character)
```

### 3. Confusing * and +
```python
r"ab*c"  # Matches: ac, abc, abbc (b is optional)
r"ab+c"  # Matches: abc, abbc (at least one b required)
```

### 4. Greedy Matching Issues
```python
# When matching HTML tags
r"<.*>"   # ✗ Too greedy
r"<.*?>"  # ✓ Non-greedy
```

### 5. Using .* with Newlines
```python
# Use DOTALL flag if you want . to match newlines
re.search(r"start.*end", text, re.DOTALL)
```

---

## 🎓 Real-World Applications

### Web Scraping
- Extract emails, phone numbers, URLs
- Parse HTML content
- Clean text data

### Data Validation
- Validate user input (email, phone, passwords)
- Check format compliance
- Sanitize data

### Text Processing
- Find and replace patterns
- Extract structured data
- Split by complex delimiters

### Log Analysis
- Parse log files
- Extract timestamps
- Find error patterns

### Data Cleaning
- Remove unwanted characters
- Normalize formats
- Standardize data

---

## ✅ Checklist for Interview Readiness

- [ ] Understand all basic patterns (., ^, $, |)
- [ ] Know character classes (\d, \w, \s)
- [ ] Master quantifiers (*, +, ?, {n,m})
- [ ] Understand groups and capturing
- [ ] Know when to use lookahead/lookbehind
- [ ] Familiar with all regex methods
- [ ] Can validate common formats (email, phone)
- [ ] Understand greedy vs non-greedy
- [ ] Know the difference between match() and search()
- [ ] Can write clean, readable regex patterns
- [ ] Understand regex flags
- [ ] Can debug regex patterns

---

## 🏆 Practice Exercises

After studying the guide, try these:

1. Write a regex to validate email addresses
2. Extract all URLs from a text
3. Validate US phone numbers in different formats
4. Remove all HTML tags from a string
5. Find all repeated words in a sentence
6. Extract dates in YYYY-MM-DD format
7. Validate password strength (8+ chars, uppercase, lowercase, digit)
8. Split text by multiple delimiters
9. Extract hashtags from social media text
10. Mask sensitive data (SSN, credit card numbers)
11. Convert CamelCase to snake_case
12. Parse CSV with regex
13. Extract IP addresses
14. Validate hex color codes
15. Find all email domains

---

## 📚 Additional Resources

- **Python re module docs:** https://docs.python.org/3/library/re.html
- **Regex101 (online tester):** https://regex101.com/
- **RegExr (visual tool):** https://regexr.com/
- **Pythex (Python-specific):** https://pythex.org/

---

## 🎯 Interview Question Bank

### Easy (Must Know)
1. How to match a specific word?
2. How to find all digits in a string?
3. How to match start/end of string?
4. What does `.` match?
5. Difference between `*` and `+`?

### Medium (Should Know)
6. How to validate an email?
7. What are capture groups?
8. How to use backreferences?
9. Difference between greedy and non-greedy?
10. What is `\b` used for?

### Hard (Good to Know)
11. What are lookahead assertions?
12. When to use VERBOSE flag?
13. How to match across multiple lines?
14. Performance optimization tips?
15. Complex password validation?

---

## 💪 You're Ready When You Can:

- ✅ Write regex patterns without googling
- ✅ Validate common formats (email, phone, URL)
- ✅ Extract specific data from text
- ✅ Transform text using regex
- ✅ Debug regex patterns
- ✅ Explain patterns to others
- ✅ Choose right method (search, match, findall)
- ✅ Use flags appropriately
- ✅ Optimize patterns for performance
- ✅ Solve interview problems confidently

---

## 🌟 Quick Start Commands

```bash
# Learn comprehensively
python regex_complete_guide.py

# Quick reference
python regex_quick_reference.py

# Practice examples
python regex_examples.py

# Test your own patterns
python -c "import re; print(re.findall(r'\d+', 'test 123'))"
```

---

## 🏆 Good Luck with Your Interviews!

Master these patterns and you'll ace any regex question! 🚀

**Remember:** Regex is a powerful tool - use it wisely and always test thoroughly!




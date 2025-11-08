"""
REGEX COMPLETE GUIDE - From Basic to Advanced
A comprehensive reference for interview preparation
Each pattern includes: Description + Example + Output + Use Cases
"""

import re
from rich.console import Console
from rich.table import Table
from rich import box

# Initialize Rich console for beautiful output
console = Console()

print("=" * 80)
print("REGEX COMPLETE GUIDE - Interview Preparation")
print("=" * 80)

# =============================================================================
# 1. BASIC PATTERNS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("1. BASIC PATTERNS", style="bold green")
console.print("=" * 80, style="bold")

# 1.1 Literal characters
console.print("\n[cyan]--- 1.1 Literal Characters - Exact match ---[/cyan]")
text = "Hello World"
pattern = r"Hello"
match = re.search(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Match: [green]{match.group() if match else 'No match'}[/green]")
console.print("[dim]Description: Matches exact string 'Hello'[/dim]")

# 1.2 Dot (.) - any character
console.print("\n[cyan]--- 1.2 Dot (.) - Match any single character ---[/cyan]")
text = "cat, bat, rat"
pattern = r".at"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: . matches any character (except newline)[/dim]")

# 1.3 Caret (^) - start of string
console.print("\n[cyan]--- 1.3 Caret (^) - Match start of string ---[/cyan]")
text = "Hello World"
pattern = r"^Hello"
match = re.search(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Match: [green]{match.group() if match else 'No match'}[/green]")
console.print("[dim]Description: ^ anchors pattern to start of string[/dim]")

# 1.4 Dollar ($) - end of string
console.print("\n[cyan]--- 1.4 Dollar ($) - Match end of string ---[/cyan]")
text = "Hello World"
pattern = r"World$"
match = re.search(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Match: [green]{match.group() if match else 'No match'}[/green]")
console.print("[dim]Description: $ anchors pattern to end of string[/dim]")

# 1.5 Pipe (|) - OR operator
console.print("\n[cyan]--- 1.5 Pipe (|) - OR operator ---[/cyan]")
text = "I have a cat and a dog"
pattern = r"cat|dog"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 'cat' OR 'dog'[/dim]")

# =============================================================================
# 2. CHARACTER CLASSES
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("2. CHARACTER CLASSES", style="bold green")
console.print("=" * 80, style="bold")

# 2.1 Square brackets [] - character set
console.print("\n[cyan]--- 2.1 [abc] - Match any character in set ---[/cyan]")
text = "cat, bat, rat, mat"
pattern = r"[cbr]at"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 'cat', 'bat', or 'rat' but not 'mat'[/dim]")

# 2.2 Range [a-z]
console.print("\n[cyan]--- 2.2 [a-z] - Match character range ---[/cyan]")
text = "a1b2c3"
pattern = r"[a-z]"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches any lowercase letter[/dim]")

# 2.3 Negated set [^abc]
console.print("\n[cyan]--- 2.3 [^abc] - Match anything NOT in set ---[/cyan]")
text = "cat, bat, rat, mat"
pattern = r"[^cbr]at"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 'mat' but not 'cat', 'bat', 'rat'[/dim]")

# 2.4 \d - digit
console.print("\n[cyan]--- 2.4 \\d - Match any digit [0-9] ---[/cyan]")
text = "Room 123, Phone: 555-1234"
pattern = r"\d+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches sequences of digits[/dim]")

# 2.5 \D - non-digit
console.print("\n[cyan]--- 2.5 \\D - Match any non-digit ---[/cyan]")
text = "abc123def456"
pattern = r"\D+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches sequences of non-digits[/dim]")

# 2.6 \w - word character
console.print("\n[cyan]--- 2.6 \\w - Match word character [a-zA-Z0-9_] ---[/cyan]")
text = "hello_world123, test-case"
pattern = r"\w+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches alphanumeric and underscore[/dim]")

# 2.7 \W - non-word character
console.print("\n[cyan]--- 2.7 \\W - Match non-word character ---[/cyan]")
text = "hello, world!"
pattern = r"\W+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches non-alphanumeric characters[/dim]")

# 2.8 \s - whitespace
console.print("\n[cyan]--- 2.8 \\s - Match whitespace (space, tab, newline) ---[/cyan]")
text = "hello world\ttab\nnewline"
pattern = r"\s+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{repr(text)}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{repr(matches)}[/green]")
console.print("[dim]Description: Matches any whitespace character[/dim]")

# 2.9 \S - non-whitespace
console.print("\n[cyan]--- 2.9 \\S - Match non-whitespace ---[/cyan]")
text = "hello world"
pattern = r"\S+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches any non-whitespace character[/dim]")

# =============================================================================
# 3. QUANTIFIERS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("3. QUANTIFIERS (How many times)", style="bold green")
console.print("=" * 80, style="bold")

# 3.1 * - zero or more
console.print("\n[cyan]--- 3.1 * - Match 0 or more times ---[/cyan]")
text = "a ab abc abbc abbbc"
pattern = r"ab*c"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 'ac', 'abc', 'abbc', etc.[/dim]")

# 3.2 + - one or more
console.print("\n[cyan]--- 3.2 + - Match 1 or more times ---[/cyan]")
text = "a ab abc abbc abbbc"
pattern = r"ab+c"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 'abc', 'abbc', etc. but not 'ac'[/dim]")

# 3.3 ? - zero or one
console.print("\n[cyan]--- 3.3 ? - Match 0 or 1 time (optional) ---[/cyan]")
text = "color colour"
pattern = r"colou?r"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches both 'color' and 'colour' (u is optional)[/dim]")

# 3.4 {n} - exactly n times
console.print("\n[cyan]--- 3.4 {{n}} - Match exactly n times ---[/cyan]")
text = "123 1234 12345"
pattern = r"\d{4}"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches exactly 4 digits[/dim]")

# 3.5 {n,} - n or more times
console.print("\n[cyan]--- 3.5 {{n,}} - Match n or more times ---[/cyan]")
text = "12 123 1234 12345"
pattern = r"\d{3,}"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 3 or more digits[/dim]")

# 3.6 {n,m} - between n and m times
console.print("\n[cyan]--- 3.6 {{n,m}} - Match between n and m times ---[/cyan]")
text = "12 123 1234 12345 123456"
pattern = r"\d{3,5}"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 3 to 5 digits[/dim]")

# 3.7 Greedy vs Non-greedy
console.print("\n[cyan]--- 3.7 Greedy (*) vs Non-greedy (*?) ---[/cyan]")
text = "<div>Hello</div><div>World</div>"
greedy = r"<div>.*</div>"
non_greedy = r"<div>.*?</div>"
match_greedy = re.findall(greedy, text)
match_non_greedy = re.findall(non_greedy, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Greedy [magenta]{greedy}[/magenta]: [green]{match_greedy}[/green]")
console.print(f"Non-greedy [magenta]{non_greedy}[/magenta]: [green]{match_non_greedy}[/green]")
console.print("[dim]Description: Greedy matches longest, non-greedy matches shortest[/dim]")

# =============================================================================
# 4. GROUPS AND CAPTURING
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("4. GROUPS AND CAPTURING", style="bold green")
console.print("=" * 80, style="bold")

# 4.1 Parentheses () - capturing group
console.print("\n[cyan]--- 4.1 (pattern) - Capturing group ---[/cyan]")
text = "John Doe, Jane Smith"
pattern = r"(\w+) (\w+)"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Captures first and last names separately[/dim]")

# 4.2 Non-capturing group (?:)
console.print("\n[cyan]--- 4.2 (?:pattern) - Non-capturing group ---[/cyan]")
text = "http://example.com https://test.com"
pattern = r"(?:http|https)://(\w+\.com)"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Groups http(s) but only captures domain[/dim]")

# 4.3 Named groups (?P<name>)
console.print("\n[cyan]--- 4.3 (?P<name>pattern) - Named group ---[/cyan]")
text = "John is 30 years old"
pattern = r"(?P<name>\w+) is (?P<age>\d+)"
match = re.search(pattern, text)
if match:
    console.print(f"Text: [yellow]{text}[/yellow]")
    console.print(f"Pattern: [magenta]{pattern}[/magenta]")
    console.print(f"Name: [green]{match.group('name')}[/green]")
    console.print(f"Age: [green]{match.group('age')}[/green]")
console.print("[dim]Description: Named groups for better readability[/dim]")

# 4.4 Backreferences \1, \2
console.print("\n[cyan]--- 4.4 \\1, \\2 - Backreferences ---[/cyan]")
text = "hello hello, world world, test"
pattern = r"(\w+) \1"  # Match repeated words
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: \\1 refers back to first captured group[/dim]")

# =============================================================================
# 5. LOOKAHEAD AND LOOKBEHIND
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("5. LOOKAHEAD AND LOOKBEHIND (Zero-width assertions)", style="bold green")
console.print("=" * 80, style="bold")

# 5.1 Positive lookahead (?=)
console.print("\n[cyan]--- 5.1 (?=pattern) - Positive lookahead ---[/cyan]")
text = "Python3.9 Java8 C++17"
pattern = r"\w+(?=\d)"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches language names followed by digits[/dim]")

# 5.2 Negative lookahead (?!)
console.print("\n[cyan]--- 5.2 (?!pattern) - Negative lookahead ---[/cyan]")
text = "Python3 Java Python Ruby"
pattern = r"Python(?!\d)"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches 'Python' NOT followed by digit[/dim]")

# 5.3 Positive lookbehind (?<=)
console.print("\n[cyan]--- 5.3 (?<=pattern) - Positive lookbehind ---[/cyan]")
text = "$100, €200, £300, 400"
pattern = r"(?<=\$)\d+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches numbers preceded by $[/dim]")

# 5.4 Negative lookbehind (?<!)
console.print("\n[cyan]--- 5.4 (?<!pattern) - Negative lookbehind ---[/cyan]")
text = "$100, €200, £300, 400"
pattern = r"(?<!\$)\d+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Pattern: [magenta]{pattern}[/magenta]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Matches numbers NOT preceded by $[/dim]")

# =============================================================================
# 6. COMMON REGEX METHODS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("6. REGEX METHODS IN PYTHON", style="bold green")
console.print("=" * 80, style="bold")

text = "Contact: john@example.com or jane@test.com"

# 6.1 re.search() - find first match
console.print("\n[cyan]--- 6.1 re.search() - Find first match ---[/cyan]")
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    console.print(f"Text: [yellow]{text}[/yellow]")
    console.print(f"First match: [green]{match.group()}[/green]")
    console.print(f"Position: [green]{match.span()}[/green]")
console.print("[dim]Description: Returns first match object or None[/dim]")

# 6.2 re.match() - match from start
console.print("\n[cyan]--- 6.2 re.match() - Match from beginning ---[/cyan]")
text2 = "john@example.com is an email"
match = re.match(pattern, text2)
console.print(f"Text: [yellow]{text2}[/yellow]")
console.print(f"Match: [green]{match.group() if match else 'No match'}[/green]")
console.print("[dim]Description: Matches only at start of string[/dim]")

# 6.3 re.findall() - find all matches
console.print("\n[cyan]--- 6.3 re.findall() - Find all matches ---[/cyan]")
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"All matches: [green]{matches}[/green]")
console.print("[dim]Description: Returns list of all matches[/dim]")

# 6.4 re.finditer() - iterator of matches
console.print("\n[cyan]--- 6.4 re.finditer() - Iterator of match objects ---[/cyan]")
for i, match in enumerate(re.finditer(pattern, text), 1):
    console.print(f"Match {i}: [green]{match.group()}[/green] at position {match.span()}")
console.print("[dim]Description: Returns iterator of match objects[/dim]")

# 6.5 re.sub() - substitute/replace
console.print("\n[cyan]--- 6.5 re.sub() - Replace matches ---[/cyan]")
text3 = "Price: $100, $200, $300"
pattern = r"\$(\d+)"
result = re.sub(pattern, r"€\1", text3)
console.print(f"Original: [yellow]{text3}[/yellow]")
console.print(f"After sub: [green]{result}[/green]")
console.print("[dim]Description: Replaces all matches with replacement[/dim]")

# 6.6 re.split() - split by pattern
console.print("\n[cyan]--- 6.6 re.split() - Split by pattern ---[/cyan]")
text4 = "apple,banana;cherry:date|elderberry"
pattern = r"[,;:|]"
result = re.split(pattern, text4)
console.print(f"Text: [yellow]{text4}[/yellow]")
console.print(f"Split result: [green]{result}[/green]")
console.print("[dim]Description: Splits string by regex pattern[/dim]")

# 6.7 re.compile() - compile pattern
console.print("\n[cyan]--- 6.7 re.compile() - Compile for reuse ---[/cyan]")
pattern_obj = re.compile(r"\d+")
text5 = "I have 10 apples and 20 oranges"
matches = pattern_obj.findall(text5)
console.print(f"Text: [yellow]{text5}[/yellow]")
console.print(f"Matches: [green]{matches}[/green]")
console.print("[dim]Description: Compile pattern for better performance[/dim]")

# =============================================================================
# 7. FLAGS/MODIFIERS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("7. FLAGS/MODIFIERS", style="bold green")
console.print("=" * 80, style="bold")

# 7.1 re.IGNORECASE (re.I)
console.print("\n[cyan]--- 7.1 re.IGNORECASE - Case-insensitive matching ---[/cyan]")
text = "Python python PYTHON"
pattern = r"python"
matches_normal = re.findall(pattern, text)
matches_ignore = re.findall(pattern, text, re.IGNORECASE)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Normal: [green]{matches_normal}[/green]")
console.print(f"IGNORECASE: [green]{matches_ignore}[/green]")
console.print("[dim]Description: Ignores case when matching[/dim]")

# 7.2 re.MULTILINE (re.M)
console.print("\n[cyan]--- 7.2 re.MULTILINE - ^ and $ match line boundaries ---[/cyan]")
text = "Hello World\nHello Python\nGoodbye World"
pattern = r"^Hello"
matches_normal = re.findall(pattern, text)
matches_multi = re.findall(pattern, text, re.MULTILINE)
console.print(f"Text: [yellow]{repr(text)}[/yellow]")
console.print(f"Normal: [green]{matches_normal}[/green]")
console.print(f"MULTILINE: [green]{matches_multi}[/green]")
console.print("[dim]Description: ^ and $ match start/end of each line[/dim]")

# 7.3 re.DOTALL (re.S)
console.print("\n[cyan]--- 7.3 re.DOTALL - Dot matches newline ---[/cyan]")
text = "Hello\nWorld"
pattern = r"Hello.World"
match_normal = re.search(pattern, text)
match_dotall = re.search(pattern, text, re.DOTALL)
console.print(f"Text: [yellow]{repr(text)}[/yellow]")
console.print(f"Normal: [green]{match_normal.group() if match_normal else 'No match'}[/green]")
console.print(f"DOTALL: [green]{match_dotall.group() if match_dotall else 'No match'}[/green]")
console.print("[dim]Description: Makes . match newline character[/dim]")

# 7.4 re.VERBOSE (re.X)
console.print("\n[cyan]--- 7.4 re.VERBOSE - Allow comments in pattern ---[/cyan]")
text = "john@example.com"
pattern = r"""
    \w+         # Username
    @           # At symbol
    \w+         # Domain
    \.          # Dot
    \w+         # Extension
"""
match = re.search(pattern, text, re.VERBOSE)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Match: [green]{match.group() if match else 'No match'}[/green]")
console.print("[dim]Description: Allows whitespace and comments in regex[/dim]")

# =============================================================================
# 8. REAL-WORLD PATTERNS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("8. REAL-WORLD PATTERNS (Interview Favorites)", style="bold green")
console.print("=" * 80, style="bold")

# 8.1 Email validation
console.print("\n[cyan]--- 8.1 Email Validation ---[/cyan]")
emails = ["john@example.com", "invalid.email", "test@domain.co.uk", "@invalid"]
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
for email in emails:
    match = re.match(pattern, email)
    status = "✓ Valid" if match else "✗ Invalid"
    console.print(f"{email:30} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.2 Phone number
console.print("\n[cyan]--- 8.2 Phone Number (US Format) ---[/cyan]")
phones = ["555-123-4567", "(555) 123-4567", "5551234567", "555.123.4567"]
pattern = r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
for phone in phones:
    match = re.match(pattern, phone)
    status = "✓ Valid" if match else "✗ Invalid"
    console.print(f"{phone:20} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.3 URL validation
console.print("\n[cyan]--- 8.3 URL Validation ---[/cyan]")
urls = ["https://www.example.com", "http://test.com/path", "ftp://file.org", "invalid"]
pattern = r"^(https?|ftp)://[\w\.-]+\.\w+(/[\w\.-]*)*/?$"
for url in urls:
    match = re.match(pattern, url)
    status = "✓ Valid" if match else "✗ Invalid"
    console.print(f"{url:35} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.4 IP Address
console.print("\n[cyan]--- 8.4 IP Address Validation ---[/cyan]")
ips = ["192.168.1.1", "255.255.255.255", "999.999.999.999", "192.168.1"]
pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
for ip in ips:
    match = re.match(pattern, ip)
    status = "✓ Valid" if match else "✗ Invalid"
    console.print(f"{ip:20} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern} (Note: Doesn't validate range 0-255)[/dim]")

# 8.5 Date formats
console.print("\n[cyan]--- 8.5 Date Formats (YYYY-MM-DD) ---[/cyan]")
dates = ["2024-01-15", "2024-1-5", "24-01-15", "2024/01/15"]
pattern = r"^\d{4}-\d{2}-\d{2}$"
for date in dates:
    match = re.match(pattern, date)
    status = "✓ Valid" if match else "✗ Invalid"
    console.print(f"{date:20} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.6 Password strength
console.print("\n[cyan]--- 8.6 Password Validation (min 8 chars, 1 upper, 1 lower, 1 digit) ---[/cyan]")
passwords = ["Password1", "weakpass", "NODIGIT", "Pass1", "StrongP@ss1"]
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
for pwd in passwords:
    match = re.match(pattern, pwd)
    status = "✓ Strong" if match else "✗ Weak"
    console.print(f"{pwd:20} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.7 Credit card (basic)
console.print("\n[cyan]--- 8.7 Credit Card Number (basic format) ---[/cyan]")
cards = ["1234-5678-9012-3456", "1234567890123456", "1234-5678-9012"]
pattern = r"^\d{4}-?\d{4}-?\d{4}-?\d{4}$"
for card in cards:
    match = re.match(pattern, card)
    status = "✓ Valid" if match else "✗ Invalid"
    console.print(f"{card:25} [{('green' if match else 'red')}]{status}[/]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.8 Extract hashtags
console.print("\n[cyan]--- 8.8 Extract Hashtags from Text ---[/cyan]")
text = "Learning #Python and #Regex is fun! #Interview #Preparation"
pattern = r"#\w+"
hashtags = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Hashtags: [green]{hashtags}[/green]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.9 Extract @mentions
console.print("\n[cyan]--- 8.9 Extract @mentions from Text ---[/cyan]")
text = "Thanks @john and @jane_doe for the help!"
pattern = r"@\w+"
mentions = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Mentions: [green]{mentions}[/green]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# 8.10 Remove HTML tags
console.print("\n[cyan]--- 8.10 Remove HTML Tags ---[/cyan]")
html = "<p>Hello <b>World</b>!</p>"
pattern = r"<[^>]+>"
clean = re.sub(pattern, "", html)
console.print(f"HTML: [yellow]{html}[/yellow]")
console.print(f"Clean: [green]{clean}[/green]")
console.print(f"[dim]Pattern: {pattern}[/dim]")

# =============================================================================
# 9. ADVANCED TECHNIQUES
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("9. ADVANCED TECHNIQUES", style="bold green")
console.print("=" * 80, style="bold")

# 9.1 Conditional replacement with function
console.print("\n[cyan]--- 9.1 re.sub() with Function ---[/cyan]")
text = "I have 10 apples and 20 oranges"
def double_number(match):
    return str(int(match.group()) * 2)
result = re.sub(r"\d+", double_number, text)
console.print(f"Original: [yellow]{text}[/yellow]")
console.print(f"Result: [green]{result}[/green]")
console.print("[dim]Description: Use function to transform matches[/dim]")

# 9.2 Extract and transform
console.print("\n[cyan]--- 9.2 Extract Names and Format ---[/cyan]")
text = "John Doe (30), Jane Smith (25)"
pattern = r"(\w+) (\w+) \((\d+)\)"
def format_person(match):
    return f"{match.group(2)}, {match.group(1)} - Age: {match.group(3)}"
result = re.sub(pattern, format_person, text)
console.print(f"Original: [yellow]{text}[/yellow]")
console.print(f"Formatted: [green]{result}[/green]")
console.print("[dim]Description: Complex transformation with groups[/dim]")

# 9.3 Validate and extract
console.print("\n[cyan]--- 9.3 Parse Log File Entry ---[/cyan]")
log = "2024-01-15 10:30:45 ERROR User login failed"
pattern = r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)$"
match = re.match(pattern, log)
if match:
    console.print(f"Log: [yellow]{log}[/yellow]")
    console.print(f"Date: [green]{match.group(1)}[/green]")
    console.print(f"Time: [green]{match.group(2)}[/green]")
    console.print(f"Level: [green]{match.group(3)}[/green]")
    console.print(f"Message: [green]{match.group(4)}[/green]")
console.print("[dim]Description: Parse structured text[/dim]")

# 9.4 Multiple patterns
console.print("\n[cyan]--- 9.4 Match Multiple Patterns ---[/cyan]")
text = "Contact: +1-555-1234 or email: john@example.com"
patterns = [
    (r"\+\d{1,3}-\d{3}-\d{4}", "Phone"),
    (r"\w+@\w+\.\w+", "Email")
]
for pattern, label in patterns:
    matches = re.findall(pattern, text)
    if matches:
        console.print(f"{label}: [green]{matches}[/green]")
console.print("[dim]Description: Apply multiple patterns to same text[/dim]")

# =============================================================================
# 10. COMMON INTERVIEW PROBLEMS
# =============================================================================
console.print("\n" + "=" * 80, style="bold")
console.print("10. COMMON INTERVIEW PROBLEMS", style="bold green")
console.print("=" * 80, style="bold")

# 10.1 Extract all integers
console.print("\n[cyan]--- 10.1 Extract All Integers (including negative) ---[/cyan]")
text = "Prices: 100, -50, +75, 200"
pattern = r"[+-]?\d+"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Integers: [green]{matches}[/green]")

# 10.2 Extract all words
console.print("\n[cyan]--- 10.2 Extract All Words ---[/cyan]")
text = "Hello, world! This is a test."
pattern = r"\b\w+\b"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Words: [green]{matches}[/green]")

# 10.3 Find repeated words
console.print("\n[cyan]--- 10.3 Find Repeated Words ---[/cyan]")
text = "This is is a test test"
pattern = r"\b(\w+)\s+\1\b"
matches = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Repeated: [green]{matches}[/green]")

# 10.4 Validate hex color
console.print("\n[cyan]--- 10.4 Validate Hex Color Code ---[/cyan]")
colors = ["#FF0000", "#abc", "#GGG", "FF0000"]
pattern = r"^#[0-9A-Fa-f]{3,6}$"
for color in colors:
    match = re.match(pattern, color)
    status = "✓" if match else "✗"
    console.print(f"{color:10} [{('green' if match else 'red')}]{status}[/]")

# 10.5 Extract domain from email
console.print("\n[cyan]--- 10.5 Extract Domain from Email ---[/cyan]")
emails = ["john@example.com", "jane@test.co.uk"]
pattern = r"@([\w\.-]+)"
for email in emails:
    match = re.search(pattern, email)
    if match:
        console.print(f"{email} → [green]{match.group(1)}[/green]")

# 10.6 Count word frequency
console.print("\n[cyan]--- 10.6 Count Word Frequency ---[/cyan]")
text = "apple banana apple cherry banana apple"
words = re.findall(r"\w+", text)
from collections import Counter
freq = Counter(words)
for word, count in freq.items():
    console.print(f"{word}: [green]{count}[/green]")

# 10.7 Split camelCase
console.print("\n[cyan]--- 10.7 Split camelCase into Words ---[/cyan]")
text = "thisIsCamelCase"
pattern = r"([A-Z][a-z]+|[a-z]+)"
words = re.findall(pattern, text)
console.print(f"CamelCase: [yellow]{text}[/yellow]")
console.print(f"Words: [green]{words}[/green]")

# 10.8 Remove extra spaces
console.print("\n[cyan]--- 10.8 Remove Extra Whitespace ---[/cyan]")
text = "Too   many    spaces"
result = re.sub(r"\s+", " ", text)
console.print(f"Original: [yellow]{text}[/yellow]")
console.print(f"Clean: [green]{result}[/green]")

# 10.9 Mask credit card
console.print("\n[cyan]--- 10.9 Mask Credit Card Number ---[/cyan]")
card = "1234-5678-9012-3456"
pattern = r"\d(?=\d{4})"
masked = re.sub(pattern, "*", card)
console.print(f"Original: [yellow]{card}[/yellow]")
console.print(f"Masked: [green]{masked}[/green]")

# 10.10 Extract version numbers
console.print("\n[cyan]--- 10.10 Extract Version Numbers ---[/cyan]")
text = "Python 3.9.7, Node 14.17.0, Java 11.0.2"
pattern = r"\d+\.\d+\.\d+"
versions = re.findall(pattern, text)
console.print(f"Text: [yellow]{text}[/yellow]")
console.print(f"Versions: [green]{versions}[/green]")

console.print("\n" + "=" * 80, style="bold")
console.print("END OF REGEX COMPLETE GUIDE", style="bold green")
console.print("=" * 80, style="bold")
console.print("\n✅ You're now ready to ace regex interviews!", style="bold green")



"""
REGEX QUICK REFERENCE CHEATSHEET
One-page summary of most important patterns
"""

import re
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

print("=" * 80)
print("REGEX QUICK REFERENCE - Most Important Patterns")
print("=" * 80)

# Create reference table
table = Table(title="Essential Regex Patterns", box=box.ROUNDED, show_header=True, header_style="bold cyan")
table.add_column("Pattern", style="magenta", width=20)
table.add_column("Description", style="yellow", width=30)
table.add_column("Example", style="green", width=25)

# Basic patterns
table.add_row(".", "Any character", "a.c matches abc, a1c")
table.add_row("^", "Start of string", "^Hello matches Hello...")
table.add_row("$", "End of string", "...world$ matches ...world")
table.add_row("|", "OR operator", "cat|dog matches cat or dog")

# Character classes
table.add_row("[abc]", "Character set", "[cbr]at matches cat, bat, rat")
table.add_row("[^abc]", "Negated set", "[^c]at matches bat, not cat")
table.add_row("[a-z]", "Range", "[0-9] matches any digit")
table.add_row("\\d", "Digit [0-9]", "\\d+ matches 123")
table.add_row("\\D", "Non-digit", "\\D+ matches abc")
table.add_row("\\w", "Word [a-zA-Z0-9_]", "\\w+ matches hello_123")
table.add_row("\\W", "Non-word", "\\W+ matches !@#")
table.add_row("\\s", "Whitespace", "\\s+ matches spaces/tabs")
table.add_row("\\S", "Non-whitespace", "\\S+ matches hello")
table.add_row("\\b", "Word boundary", "\\bcat\\b matches cat not catdog")

# Quantifiers
table.add_row("*", "0 or more", "ab*c matches ac, abc, abbc")
table.add_row("+", "1 or more", "ab+c matches abc, abbc")
table.add_row("?", "0 or 1 (optional)", "colou?r matches color, colour")
table.add_row("{n}", "Exactly n", "\\d{4} matches 1234")
table.add_row("{n,}", "n or more", "\\d{3,} matches 123, 1234")
table.add_row("{n,m}", "Between n and m", "\\d{2,4} matches 12, 123, 1234")
table.add_row("*?", "Non-greedy *", "<.*?> matches <div>, not <div>...</div>")

# Groups
table.add_row("(abc)", "Capture group", "(\\d+)-(\\d+) captures parts")
table.add_row("(?:abc)", "Non-capturing", "(?:https?):// groups but doesn't capture")
table.add_row("(?P<name>)", "Named group", "(?P<year>\\d{4})")
table.add_row("\\1, \\2", "Backreference", "(\\w+) \\1 matches hello hello")

# Lookahead/Lookbehind
table.add_row("(?=abc)", "Positive lookahead", "\\w+(?=\\d) matches Python in Python3")
table.add_row("(?!abc)", "Negative lookahead", "Python(?!\\d) matches Python not Python3")
table.add_row("(?<=abc)", "Positive lookbehind", "(?<=\\$)\\d+ matches 100 in $100")
table.add_row("(?<!abc)", "Negative lookbehind", "(?<!\\$)\\d+ matches 100 not in $100")

console.print(table)

# Python methods
console.print("\n[bold]📚 PYTHON REGEX METHODS[/bold]")
console.print("=" * 80)

methods_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
methods_table.add_column("Method", style="magenta", width=25)
methods_table.add_column("Description", style="yellow", width=50)

methods_table.add_row("re.search(pattern, text)", "Find first match anywhere in string")
methods_table.add_row("re.match(pattern, text)", "Match pattern at start of string")
methods_table.add_row("re.findall(pattern, text)", "Return list of all matches")
methods_table.add_row("re.finditer(pattern, text)", "Return iterator of match objects")
methods_table.add_row("re.sub(pattern, repl, text)", "Replace matches with replacement")
methods_table.add_row("re.split(pattern, text)", "Split string by pattern")
methods_table.add_row("re.compile(pattern)", "Compile pattern for reuse")

console.print(methods_table)

# Flags
console.print("\n[bold]🚩 COMMON FLAGS[/bold]")
console.print("=" * 80)

flags_table = Table(box=box.SIMPLE, show_header=True, header_style="bold cyan")
flags_table.add_column("Flag", style="magenta", width=25)
flags_table.add_column("Description", style="yellow", width=50)

flags_table.add_row("re.IGNORECASE (re.I)", "Case-insensitive matching")
flags_table.add_row("re.MULTILINE (re.M)", "^ and $ match line boundaries")
flags_table.add_row("re.DOTALL (re.S)", "Dot matches newline")
flags_table.add_row("re.VERBOSE (re.X)", "Allow comments and whitespace in pattern")

console.print(flags_table)

# Real-world patterns
console.print("\n[bold]🎯 TOP 10 REAL-WORLD PATTERNS[/bold]")
console.print("=" * 80)

patterns = [
    ("Email", r'^[\w\.-]+@[\w\.-]+\.\w+$', "john@example.com"),
    ("Phone (US)", r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$', "555-123-4567"),
    ("URL", r'^(https?|ftp)://[\w\.-]+\.\w+(/[\w\.-]*)*/?$', "https://example.com"),
    ("IP Address", r'^(\d{1,3}\.){3}\d{1,3}$', "192.168.1.1"),
    ("Date (YYYY-MM-DD)", r'^\d{4}-\d{2}-\d{2}$', "2024-01-15"),
    ("Time (HH:MM)", r'^([01]\d|2[0-3]):([0-5]\d)$', "14:30"),
    ("Hex Color", r'^#[0-9A-Fa-f]{3,6}$', "#FF5733"),
    ("Username", r'^[a-zA-Z0-9_]{3,16}$', "user_123"),
    ("Password", r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', "Pass123!"),
    ("Hashtag", r'#\w+', "#Python"),
]

for name, pattern, example in patterns:
    console.print(f"[cyan]{name:20}[/cyan] [magenta]{pattern:50}[/magenta] [green]Ex: {example}[/green]")

# Live examples
console.print("\n[bold]💻 LIVE EXAMPLES[/bold]")
console.print("=" * 80)

# Example 1: Extract emails
console.print("\n[yellow]1. Extract Email Addresses[/yellow]")
text = "Contact: john@example.com or jane@test.com"
emails = re.findall(r'\w+@\w+\.\w+', text)
console.print(f"Text: {text}")
console.print(f"Emails: [green]{emails}[/green]")

# Example 2: Validate phone
console.print("\n[yellow]2. Validate Phone Number[/yellow]")
phone = "555-123-4567"
pattern = r'^\d{3}-\d{3}-\d{4}$'
is_valid = bool(re.match(pattern, phone))
console.print(f"Phone: {phone}")
console.print(f"Valid: [{'green' if is_valid else 'red'}]{is_valid}[/]")

# Example 3: Replace
console.print("\n[yellow]3. Replace/Mask Sensitive Data[/yellow]")
text = "My SSN is 123-45-6789"
masked = re.sub(r'\d{3}-\d{2}-\d{4}', '***-**-****', text)
console.print(f"Original: {text}")
console.print(f"Masked: [green]{masked}[/green]")

# Example 4: Extract numbers
console.print("\n[yellow]4. Extract All Numbers[/yellow]")
text = "I have 10 apples and 20 oranges"
numbers = re.findall(r'\d+', text)
console.print(f"Text: {text}")
console.print(f"Numbers: [green]{numbers}[/green]")

# Example 5: Split by multiple delimiters
console.print("\n[yellow]5. Split by Multiple Delimiters[/yellow]")
text = "apple,banana;cherry:date|grape"
fruits = re.split(r'[,;:|]', text)
console.print(f"Text: {text}")
console.print(f"Fruits: [green]{fruits}[/green]")

# Example 6: Find repeated words
console.print("\n[yellow]6. Find Repeated Words[/yellow]")
text = "This is is a test test"
pattern = r'\b(\w+)\s+\1\b'
repeated = re.findall(pattern, text)
console.print(f"Text: {text}")
console.print(f"Repeated: [green]{repeated}[/green]")

# Example 7: Remove HTML tags
console.print("\n[yellow]7. Remove HTML Tags[/yellow]")
html = "<p>Hello <b>World</b>!</p>"
clean = re.sub(r'<[^>]+>', '', html)
console.print(f"HTML: {html}")
console.print(f"Clean: [green]{clean}[/green]")

# Example 8: Extract hashtags
console.print("\n[yellow]8. Extract Hashtags[/yellow]")
text = "Learning #Python #Regex #Interview"
hashtags = re.findall(r'#\w+', text)
console.print(f"Text: {text}")
console.print(f"Hashtags: [green]{hashtags}[/green]")

# Example 9: Parse CSV line
console.print("\n[yellow]9. Parse Simple CSV[/yellow]")
csv_line = "John,Doe,30,Engineer"
fields = re.split(r',', csv_line)
console.print(f"CSV: {csv_line}")
console.print(f"Fields: [green]{fields}[/green]")

# Example 10: Camel case to snake case
console.print("\n[yellow]10. CamelCase to snake_case[/yellow]")
camel = "thisIsCamelCase"
snake = re.sub(r'(?<!^)(?=[A-Z])', '_', camel).lower()
console.print(f"CamelCase: {camel}")
console.print(f"snake_case: [green]{snake}[/green]")

# Interview Tips
console.print("\n[bold]💡 INTERVIEW TIPS[/bold]")
console.print("=" * 80)

tips = [
    "Always use raw strings (r'pattern') to avoid escaping issues",
    "Test your regex with multiple test cases (valid and invalid)",
    "Use re.compile() when reusing patterns for better performance",
    "Remember: Greedy (*) vs Non-greedy (*?)",
    "Use named groups (?P<name>) for readability",
    "Lookahead/Lookbehind are zero-width (don't consume characters)",
    "\\b is for word boundaries, not the backspace character",
    "Use re.VERBOSE for complex patterns with comments",
    "Always validate user input, don't rely solely on regex",
    "Know the difference between re.match() and re.search()",
]

for i, tip in enumerate(tips, 1):
    console.print(f"[cyan]{i:2}.[/cyan] {tip}")

# Common mistakes
console.print("\n[bold]⚠️  COMMON MISTAKES[/bold]")
console.print("=" * 80)

mistakes = [
    ("Forgetting raw strings", "Wrong: '\\d+', Right: r'\\d+'"),
    ("Greedy matching", "Use .*? instead of .* for shortest match"),
    ("Not escaping special chars", "Use \\. to match literal dot"),
    ("Using .* across lines", "Use re.DOTALL flag if needed"),
    ("Forgetting anchors", "Use ^ and $ to match entire string"),
]

for mistake, solution in mistakes:
    console.print(f"[red]✗[/red] {mistake:30} [green]→[/green] {solution}")

console.print("\n" + "=" * 80)
console.print("✅ You're ready for regex interviews!", style="bold green")
console.print("=" * 80)




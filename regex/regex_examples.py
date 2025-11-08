"""
REGEX EXAMPLES - Your Working File
Practice and experiment with regex patterns here
"""

import re
from rich.console import Console
from rich import box
from rich.table import Table

console = Console()

console.print("[bold green]🎯 REGEX PRACTICE EXAMPLES[/bold green]")
console.print("=" * 80)

# =============================================================================
# BASIC EXAMPLES
# =============================================================================

console.print("\n[bold cyan]📚 BASIC PATTERNS[/bold cyan]")
console.print("-" * 80)

# Example 1: Simple search
text1 = "The quick brown fox jumps over the lazy dog"
pattern1 = r"fox"
match1 = re.search(pattern1, text1)
console.print(f"\n[yellow]Example 1: Simple Search[/yellow]")
console.print(f"Text: {text1}")
console.print(f"Pattern: {pattern1}")
console.print(f"Found: [green]{match1.group() if match1 else 'Not found'}[/green]")

# Example 2: Find all words
text2 = "Hello World, Python Programming!"
pattern2 = r"\b\w+\b"
matches2 = re.findall(pattern2, text2)
console.print(f"\n[yellow]Example 2: Find All Words[/yellow]")
console.print(f"Text: {text2}")
console.print(f"Pattern: {pattern2}")
console.print(f"Words: [green]{matches2}[/green]")

# Example 3: Find all digits
text3 = "Order #123, Quantity: 45, Price: $67.89"
pattern3 = r"\d+"
matches3 = re.findall(pattern3, text3)
console.print(f"\n[yellow]Example 3: Find All Numbers[/yellow]")
console.print(f"Text: {text3}")
console.print(f"Pattern: {pattern3}")
console.print(f"Numbers: [green]{matches3}[/green]")

# Example 4: Replace text
text4 = "Hello World"
pattern4 = r"World"
replacement4 = "Python"
result4 = re.sub(pattern4, replacement4, text4)
console.print(f"\n[yellow]Example 4: Replace Text[/yellow]")
console.print(f"Original: {text4}")
console.print(f"Pattern: {pattern4} → {replacement4}")
console.print(f"Result: [green]{result4}[/green]")

# =============================================================================
# VALIDATION EXAMPLES
# =============================================================================

console.print("\n[bold cyan]✅ VALIDATION PATTERNS[/bold cyan]")
console.print("-" * 80)

# Email validation
console.print(f"\n[yellow]Email Validation[/yellow]")
emails = [
    "valid@example.com",
    "user.name@test.co.uk",
    "invalid@",
    "@invalid.com",
    "no-at-sign.com"
]
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
for email in emails:
    is_valid = bool(re.match(email_pattern, email))
    status = "✓" if is_valid else "✗"
    color = "green" if is_valid else "red"
    console.print(f"  [{color}]{status}[/] {email}")

# Phone validation
console.print(f"\n[yellow]Phone Number Validation (US)[/yellow]")
phones = [
    "555-123-4567",
    "(555) 123-4567",
    "5551234567",
    "123-4567",
]
phone_pattern = r"^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$"
for phone in phones:
    is_valid = bool(re.match(phone_pattern, phone))
    status = "✓" if is_valid else "✗"
    color = "green" if is_valid else "red"
    console.print(f"  [{color}]{status}[/] {phone}")

# URL validation
console.print(f"\n[yellow]URL Validation[/yellow]")
urls = [
    "https://www.example.com",
    "http://test.com/path/to/page",
    "ftp://files.server.org",
    "not-a-url",
]
url_pattern = r"^(https?|ftp)://[\w\.-]+\.\w+(/[\w\.-]*)*/?$"
for url in urls:
    is_valid = bool(re.match(url_pattern, url))
    status = "✓" if is_valid else "✗"
    color = "green" if is_valid else "red"
    console.print(f"  [{color}]{status}[/] {url}")

# =============================================================================
# EXTRACTION EXAMPLES
# =============================================================================

console.print("\n[bold cyan]📤 EXTRACTION PATTERNS[/bold cyan]")
console.print("-" * 80)

# Extract emails from text
console.print(f"\n[yellow]Extract Email Addresses[/yellow]")
text_with_emails = "Contact us at support@example.com or sales@company.co.uk for help"
email_extract_pattern = r"\w+@\w+\.\w+"
extracted_emails = re.findall(email_extract_pattern, text_with_emails)
console.print(f"Text: {text_with_emails}")
console.print(f"Emails: [green]{extracted_emails}[/green]")

# Extract hashtags
console.print(f"\n[yellow]Extract Hashtags[/yellow]")
social_text = "Learning #Python #Regex for #DataScience and #MachineLearning!"
hashtag_pattern = r"#\w+"
hashtags = re.findall(hashtag_pattern, social_text)
console.print(f"Text: {social_text}")
console.print(f"Hashtags: [green]{hashtags}[/green]")

# Extract mentions
console.print(f"\n[yellow]Extract @mentions[/yellow]")
tweet = "Thanks @john_doe and @jane_smith for the amazing work!"
mention_pattern = r"@\w+"
mentions = re.findall(mention_pattern, tweet)
console.print(f"Text: {tweet}")
console.print(f"Mentions: [green]{mentions}[/green]")

# Extract dates
console.print(f"\n[yellow]Extract Dates (YYYY-MM-DD)[/yellow]")
log_text = "Events on 2024-01-15, 2024-02-20, and 2024-03-25"
date_pattern = r"\d{4}-\d{2}-\d{2}"
dates = re.findall(date_pattern, log_text)
console.print(f"Text: {log_text}")
console.print(f"Dates: [green]{dates}[/green]")

# =============================================================================
# TRANSFORMATION EXAMPLES
# =============================================================================

console.print("\n[bold cyan]🔄 TRANSFORMATION PATTERNS[/bold cyan]")
console.print("-" * 80)

# Remove HTML tags
console.print(f"\n[yellow]Remove HTML Tags[/yellow]")
html_text = "<h1>Title</h1><p>This is a <b>bold</b> paragraph.</p>"
html_pattern = r"<[^>]+>"
clean_text = re.sub(html_pattern, "", html_text)
console.print(f"HTML: {html_text}")
console.print(f"Clean: [green]{clean_text}[/green]")

# Remove extra spaces
console.print(f"\n[yellow]Remove Extra Whitespace[/yellow]")
messy_text = "Too    many     spaces    here"
space_pattern = r"\s+"
clean_spaces = re.sub(space_pattern, " ", messy_text)
console.print(f"Original: {messy_text}")
console.print(f"Clean: [green]{clean_spaces}[/green]")

# Mask credit card
console.print(f"\n[yellow]Mask Credit Card Number[/yellow]")
credit_card = "1234-5678-9012-3456"
mask_pattern = r"\d(?=\d{4})"
masked_card = re.sub(mask_pattern, "*", credit_card)
console.print(f"Original: {credit_card}")
console.print(f"Masked: [green]{masked_card}[/green]")

# CamelCase to snake_case
console.print(f"\n[yellow]CamelCase to snake_case[/yellow]")
camel_text = "thisIsCamelCaseText"
snake_result = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_text).lower()
console.print(f"CamelCase: {camel_text}")
console.print(f"snake_case: [green]{snake_result}[/green]")

# =============================================================================
# ADVANCED EXAMPLES
# =============================================================================

console.print("\n[bold cyan]🚀 ADVANCED PATTERNS[/bold cyan]")
console.print("-" * 80)

# Parse log file
console.print(f"\n[yellow]Parse Log Entry[/yellow]")
log_entry = "2024-01-15 14:30:45 ERROR Database connection failed"
log_pattern = r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)$"
log_match = re.match(log_pattern, log_entry)
if log_match:
    console.print(f"Log: {log_entry}")
    console.print(f"Date: [green]{log_match.group(1)}[/green]")
    console.print(f"Time: [green]{log_match.group(2)}[/green]")
    console.print(f"Level: [green]{log_match.group(3)}[/green]")
    console.print(f"Message: [green]{log_match.group(4)}[/green]")

# Extract name parts
console.print(f"\n[yellow]Extract Name Components[/yellow]")
full_name = "John Michael Doe"
name_pattern = r"^(\w+)\s+(\w+)\s+(\w+)$"
name_match = re.match(name_pattern, full_name)
if name_match:
    console.print(f"Full Name: {full_name}")
    console.print(f"First: [green]{name_match.group(1)}[/green]")
    console.print(f"Middle: [green]{name_match.group(2)}[/green]")
    console.print(f"Last: [green]{name_match.group(3)}[/green]")

# Find repeated words
console.print(f"\n[yellow]Find Repeated Words[/yellow]")
repeated_text = "This is is a test test of repeated repeated words"
repeated_pattern = r"\b(\w+)\s+\1\b"
repeated_words = re.findall(repeated_pattern, repeated_text)
console.print(f"Text: {repeated_text}")
console.print(f"Repeated: [green]{repeated_words}[/green]")

# Split by multiple delimiters
console.print(f"\n[yellow]Split by Multiple Delimiters[/yellow]")
delimited_text = "apple,banana;cherry:date|elderberry"
delimiter_pattern = r"[,;:|]"
split_fruits = re.split(delimiter_pattern, delimited_text)
console.print(f"Text: {delimited_text}")
console.print(f"Split: [green]{split_fruits}[/green]")

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

console.print("\n[bold cyan]💼 PRACTICAL APPLICATIONS[/bold cyan]")
console.print("-" * 80)

# Validate password strength
console.print(f"\n[yellow]Password Strength Checker[/yellow]")
console.print("[dim]Requirements: 8+ chars, 1 uppercase, 1 lowercase, 1 digit[/dim]")
passwords = ["weak", "Strong1", "NoDigit", "short1A", "ValidPass123"]
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
for pwd in passwords:
    is_strong = bool(re.match(password_pattern, pwd))
    status = "✓ Strong" if is_strong else "✗ Weak"
    color = "green" if is_strong else "red"
    console.print(f"  [{color}]{status}[/] {pwd}")

# Extract and format phone numbers
console.print(f"\n[yellow]Standardize Phone Numbers[/yellow]")
mixed_phones = ["5551234567", "555-123-4567", "(555) 123-4567"]
phone_extract = r"(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})"
for phone in mixed_phones:
    match = re.search(r"\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})", phone)
    if match:
        formatted = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
        console.print(f"  {phone:20} → [green]{formatted}[/green]")

# Extract domain from URLs
console.print(f"\n[yellow]Extract Domains from URLs[/yellow]")
url_list = ["https://www.example.com/page", "http://test.org", "ftp://files.server.net"]
domain_pattern = r"://(?:www\.)?([^/]+)"
for url in url_list:
    match = re.search(domain_pattern, url)
    if match:
        console.print(f"  {url:35} → [green]{match.group(1)}[/green]")

# =============================================================================
# PRACTICE AREA
# =============================================================================

console.print("\n[bold cyan]✏️  YOUR PRACTICE AREA[/bold cyan]")
console.print("-" * 80)
console.print("\n[yellow]Add your own examples below and experiment![/yellow]\n")

# Your practice code here
# Example:
# my_text = "Your text here"
# my_pattern = r"your pattern"
# result = re.findall(my_pattern, my_text)
# console.print(f"Result: [green]{result}[/green]")

console.print("\n" + "=" * 80)
console.print("[bold green]✅ Great practice! Keep experimenting with regex![/bold green]")
console.print("=" * 80)




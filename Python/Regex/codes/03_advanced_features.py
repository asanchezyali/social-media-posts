"""
Advanced Regular Expression Features

This file demonstrates advanced regex features including groups,
lookahead/lookbehind assertions, substitutions, and more.

Try your regex online: regex101.com, pythex.org, regexr.com
"""

import re
from typing import List, Tuple


def parse_log_entry(log_line: str) -> dict:
    """Parse a log entry using named capture groups."""
    pattern = r"""
        ^                           # Start of line
        (?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\s+  # Date and time
        \[(?P<level>INFO|WARN|ERROR)\]\s+                 # Log level
        \[(?P<module>[\w.-]+)\]\s+                        # Module name
        (?P<message>.+)$                                  # Log message
    """
    match = re.match(pattern, log_line, re.VERBOSE)
    return match.groupdict() if match else {}


# Example with named groups
log_line = "2025-05-10 14:30 [ERROR] [user.auth] Failed login attempt"
parsed = parse_log_entry(log_line)
print("Parsed Log Entry:")
for key, value in parsed.items():
    print(f"{key}: {value}")


def extract_methods(code: str) -> List[Tuple[str, str]]:
    """Extract method names and their return types using lookahead."""
    pattern = r"def\s+(\w+)\s*\([^)]*\)\s*->\s*([^:]+):"
    return re.findall(pattern, code)


# Example with method extraction
python_code = """
def calculate_total(items: List[float]) -> float:
    pass

def process_data(data: dict) -> List[str]:
    pass
"""

print("\nExtracted Methods:")
for method, return_type in extract_methods(python_code):
    print(f"Method: {method}, Returns: {return_type}")


# Example with substitution and backreferences
def clean_text(text: str) -> str:
    """Clean text by removing repeated words using backreference."""
    pattern = r"\b(\w+)\s+\1\b"  # Pattern for repeated words
    return re.sub(pattern, r"\1", text)


text = "The the quick quick brown fox"
cleaned = clean_text(text)
print(f"\nOriginal text: {text}")
print(f"Cleaned text: {cleaned}")


# Example with positive/negative lookahead
def find_prices(text: str) -> None:
    """Find prices with different currencies using capturing groups."""
    # Matches numbers (with optional decimals), optional spaces, and currency
    pattern = r"(\d+(?:\.\d+)?)(?:\s*)(USD|EUR|GBP)"
    print("\nPrices found:")
    for match in re.finditer(pattern, text):
        amount = match.group(1)
        currency = match.group(2)
        print(f"Amount: {amount}, Currency: {currency}")


text = "The price is 100 USD, 200 EUR, and 150 GBP"
find_prices(text)


# Greedy vs. non-greedy matching
html = "<div>content1</div><div>content2</div>"
greedy = re.findall(r"<div>.*</div>", html)
non_greedy = re.findall(r"<div>.*?</div>", html)
print(f"\nGreedy match: {greedy}")
print(f"Non-greedy match: {non_greedy}")


# Non-capturing groups and negative lookahead
text2 = "foo1 bar1 foo2 bar2"
pattern_noncap = r"(?:foo|bar)\d"
pattern_neg_lookahead = r"foo(?!2)\d"
print(f"\nNon-capturing group matches: {re.findall(pattern_noncap, text2)}")
print(f"Negative lookahead matches (no foo2): {re.findall(pattern_neg_lookahead, text2)}")


# Negative lookbehind (fixed-width)
text3 = "abc123 xyz123 abc456"
pattern_neg_lookbehind = r"(?<!abc)123"
print(f"\nNegative lookbehind matches (not after 'abc'): {re.findall(pattern_neg_lookbehind, text3)}")


# Unicode and multiline example
unicode_text = "Café\nnaïve\nRésumé"
pattern_unicode = r"^\w+"
print(f"\nUnicode word matches (MULTILINE): {re.findall(pattern_unicode, unicode_text, re.MULTILINE | re.UNICODE)}")


# Error handling example
try:
    re.compile(r"(unclosed[")
except re.error as e:
    print(f"\nRegex error caught: {e}")

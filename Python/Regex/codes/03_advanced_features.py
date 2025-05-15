"""
Advanced Regular Expression Features

This file demonstrates advanced regex features including groups,
lookahead/lookbehind assertions, and substitutions.
"""
import re
from typing import List, Tuple

def parse_log_entry(log_line: str) -> dict:
    """Parse a log entry using named capture groups."""
    pattern = r"""
        ^                           # Start of line
        (?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\s+  # Date and time
        \[(?P<level>INFO|WARN|ERROR)\]\s+                  # Log level
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
python_code = '''
def calculate_total(items: List[float]) -> float:
    pass

def process_data(data: dict) -> List[str]:
    pass
'''

print("\nExtracted Methods:")
for method, return_type in extract_methods(python_code):
    print(f"Method: {method}, Returns: {return_type}")

# Example with substitution and backreferences
def clean_text(text: str) -> str:
    """Clean text by removing repeated words."""
    pattern = r'\b(\w+)\s+\1\b'  # Pattern for repeated words
    return re.sub(pattern, r'\1', text)

text = "The the quick quick brown fox"
cleaned = clean_text(text)
print(f"\nOriginal text: {text}")
print(f"Cleaned text: {cleaned}")

# Example with positive/negative lookahead
def find_prices(text: str) -> None:
    """Find prices with different currencies using lookahead."""
    # Matches numbers followed by USD, EUR, or GBP
    prices = re.finditer(r'\d+(?=\s*(?:USD|EUR|GBP))', text)
    print("\nPrices found:")
    for match in prices:
        price = match.group()
        # Look ahead to get the currency
        currency = re.search(r'(?<=\d\s*)(USD|EUR|GBP)', text[match.start():])
        if currency:
            print(f"Amount: {price}, Currency: {currency.group()}")
"""
Groups and Captures in Regex

This file demonstrates how to use groups and captures in regex patterns.
"""
import re

# Named groups
log_pattern = r"""
    (?P<date>\d{4}-\d{2}-\d{2})\s+  # Date in YYYY-MM-DD format
    (?P<time>\d{2}:\d{2}:\d{2})\s+  # Time in HH:MM:SS format
    (?P<level>\w+):\s+              # Log level
    (?P<message>.+)                 # Log message
"""

log_entry = "2025-05-08 14:30:00 ERROR: Database connection failed"
match = re.match(log_pattern, log_entry, re.VERBOSE)

if match:
    print("Log Entry Components:")
    print(f"Date: {match.group('date')}")
    print(f"Time: {match.group('time')}")
    print(f"Level: {match.group('level')}")
    print(f"Message: {match.group('message')}")

# Capturing and replacing
def repl_func(match):
    """Replace function for re.sub"""
    return f"'{match.group().upper()}'"

text = "The cat and the dog"
pattern = r'\b(cat|dog)\b'
result = re.sub(pattern, repl_func, text)
print(f"\nReplaced text: {result}")

# Back references
def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome using regex."""
    # Remove non-alphanumeric characters and convert to lowercase
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    # Use backreference to match reversed string
    return bool(re.match(r'^(.*?)\1?$', clean_text[::-1]))

test_strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "Was it a car or a cat I saw?"
]

print("\nPalindrome Detection:")
for text in test_strings:
    print(f"'{text}': {'✓' if is_palindrome(text) else '✗'}")
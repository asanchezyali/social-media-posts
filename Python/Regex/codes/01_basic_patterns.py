"""
Basic Pattern Matching in Python

This file demonstrates fundamental regex patterns and matching.
"""
import re

def display_match(pattern: str, text: str, description: str) -> None:
    """Helper function to display regex matches."""
    matches = re.findall(pattern, text)
    print(f"\n{description}:")
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")

# Basic pattern matching
text1 = "The quick brown fox jumps over the lazy dog"
pattern1 = r"fox"
match = re.search(pattern1, text1)
print(f"Simple match - found '{pattern1}' at position: {match.start()}-{match.end()}")

# Case-insensitive matching
pattern2 = r"FOX"
match = re.search(pattern2, text1, re.IGNORECASE)
print(f"\nCase-insensitive match found: {match.group()}")

# Word boundaries
text2 = "firefox is not a fox but firefox contains fox"
display_match(r"\bfox\b", text2, "Words that are exactly 'fox'")

# Multiple patterns using |
text3 = "The cat and the dog play with another cat"
display_match(r"cat|dog", text3, "Finding 'cat' or 'dog'")
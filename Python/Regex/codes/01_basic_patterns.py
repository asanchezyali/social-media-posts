"""
Basic Pattern Matching in Python

This file demonstrates fundamental regex patterns and matching.

Quick Reference:
.        Any character except newline
*        Zero or more repetitions
+        One or more repetitions
?        Zero or one repetition
[a-z]    Any lowercase letter
[A-Z]    Any uppercase letter
[0-9]    Any digit
\d       Digit (0-9)
\w       Word character (a-z, A-Z, 0-9, _)
\s       Whitespace
^        Start of string
$        End of string
|        Alternation (or)
()       Grouping

Try your regex online: regex101.com, pythex.org, regexr.com
"""
import re

def display_match(pattern: str, text: str, description: str) -> None:
    """Helper function to display regex matches."""
    matches = re.findall(pattern, text)
    print(f"\n{description}:")
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")

# Visual Example 1: Simple match
text1 = "The quick brown fox jumps over the lazy dog"
pattern1 = r"fox"
match = re.search(pattern1, text1)
print(f"Simple match - found '{pattern1}' at position: {match.start()}-{match.end()}")

# Visual Example 2: Case-insensitive matching
pattern2 = r"FOX"
match = re.search(pattern2, text1, re.IGNORECASE)
print(f"\nCase-insensitive match found: {match.group()}")

# Visual Example 3: Word boundaries
text2 = "firefox is not a fox but firefox contains fox"
pattern3 = r"\bfox\b"
matches = re.findall(pattern3, text2)
print(f"\nWords that are exactly 'fox': {matches}")

# Visual Example 4: Multiple patterns using |
text3 = "The cat and the dog play with another cat"
pattern4 = r"cat|dog"
matches = re.findall(pattern4, text3)
print(f"\nFinding 'cat' or 'dog': {matches}")

# Visual Example 5: Greedy vs. non-greedy matching
text4 = "<tag>content</tag>"
greedy_pattern = r"<.*>"
non_greedy_pattern = r"<.*?>"
print(f"\nGreedy match: {re.findall(greedy_pattern, text4)}")
print(f"Non-greedy match: {re.findall(non_greedy_pattern, text4)}")

# Visual Example 6: ASCII word matching (replaces Unicode example)
text5 = "Cafe naive resume"
pattern5 = r"\w+"
print(f"\nASCII word matches (default): {re.findall(pattern5, text5)}")
print(f"ASCII word matches (with re.UNICODE): {re.findall(pattern5, text5, re.UNICODE)}")
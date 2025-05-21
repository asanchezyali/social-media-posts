"""
Common Pattern Validation Examples

This file demonstrates how to validate common text patterns using regex.

Try your regex online: regex101.com, pythex.org, regexr.com
"""
import re

def validate_pattern(pattern: str, text: str) -> str:
    """Helper function to validate if text matches pattern."""
    try:
        return "[VALID]" if re.match(pattern, text) else "[INVALID]"
    except re.error as e:
        print(f"Regex error: {e}")
        return "[ERROR]"

# Email validation
# Pattern: [alphanumeric and special]@[domain].[TLD]
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
emails = [
    "user@example.com",
    "invalid.email@com",
    "name.surname+tag@domain.co.uk",
    "@invalid.com",
    "spaces are@not.allowed.com"
]

print("Email Validation:")
for email in emails:
    print(f"{email}: {validate_pattern(email_pattern, email)}")

# Phone number validation
# Pattern: optional +, optional 1, 9-15 digits
description = "Phone number: optional +, optional 1, 9-15 digits"
phone_pattern = r"^\+?1?\d{9,15}$"
phones = [
    "+1234567890",
    "123-456-7890",
    "12345",
    "+442012345678"
]

print("\nPhone Number Validation:")
for phone in phones:
    print(f"{phone}: {validate_pattern(phone_pattern, phone)}")

# URL validation
# Pattern: http(s)://... (basic)
url_pattern = r"https?://(?:[\w.-]+\.)+[\w.-]+(?:/[\w./?%&=-]*)?$"
urls = [
    "https://www.example.com",
    "http://sub.domain.co.uk/path?param=value",
    "not-a-url.com",
    "https://api.site.com/v1/data.json"
]

print("\nURL Validation:")
for url in urls:
    print(f"{url}: {validate_pattern(url_pattern, url)}")

# Date validation (YYYY-MM-DD)
# Pattern: 4 digits-2 digits-2 digits, with month/day checks
date_pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
dates = [
    "2025-12-31",
    "2025-13-01",
    "2025-04-31",
    "25-12-31"
]

print("\nDate Validation (YYYY-MM-DD):")
for date in dates:
    print(f"{date}: {validate_pattern(date_pattern, date)}")

# Multiline and DOTALL flag demonstration
multiline_text = """First line
Second line
Third line"""
pattern_multiline = r"^Second"
print("\nMultiline flag demo:")
print(re.findall(pattern_multiline, multiline_text, re.MULTILINE))

pattern_dotall = r"First.*Third"
print("DOTALL flag demo:")
print(re.findall(pattern_dotall, multiline_text, re.DOTALL))

# Common extraction recipes
sample_text = "Contact: user@example.com, visit https://site.com, call +1234567890, date 2025-12-31."
print("\nExtract emails:", re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", sample_text))
print("Extract URLs:", re.findall(r"https?://[\w.-]+(?:/[\w./?%&=-]*)?", sample_text))
print("Extract dates:", re.findall(r"\d{4}-\d{2}-\d{2}", sample_text))
print("Extract phone numbers:", re.findall(r"\+?1?\d{9,15}", sample_text))
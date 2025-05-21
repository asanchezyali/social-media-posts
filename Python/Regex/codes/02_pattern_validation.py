"""
Common Pattern Validation Examples

This file demonstrates how to validate common text patterns using regex.
"""
import re

def validate_pattern(pattern: str, text: str) -> str:
    """Helper function to validate if text matches pattern."""
    return "[VALID]" if re.match(pattern, text) else "[INVALID]"

# Email validation
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
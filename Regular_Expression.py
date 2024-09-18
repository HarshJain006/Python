# Regular Expressions in Python

## 1. What is a Regular Expression (Regex)?
# A regular expression (regex) is a sequence of characters that forms a search pattern. It is used to match strings based on specific patterns.
# In Python, the `re` module is used for working with regular expressions.

import re

# Example of a simple regex:
pattern = r'hello'
text = 'hello world'
match = re.search(pattern, text)
print(match)  # Output: <re.Match object; span=(0, 5), match='hello'>


## 2. Common Regex Functions
# Python's `re` module provides several functions for working with regular expressions.

# - `re.search()`: Searches for the pattern in the given string.
# - `re.match()`: Matches the pattern at the start of the string.
# - `re.findall()`: Returns all matches of the pattern in the string.
# - `re.sub()`: Replaces matches with a specified string.

# Example:
pattern = r'world'
text = 'hello world, welcome to the world of Python'
matches = re.findall(pattern, text)
print(matches)  # Output: ['world', 'world']


## 3. Special Characters in Regex
# Regex includes special characters that have unique meanings.

# | Character | Description                                 |
# |-----------|---------------------------------------------|
# | `.`       | Matches any character except newline.       |
# | `^`       | Matches the start of a string.              |
# | `$`       | Matches the end of a string.                |
# | `*`       | Matches 0 or more repetitions of the preceding pattern. |
# | `+`       | Matches 1 or more repetitions of the preceding pattern. |
# | `?`       | Matches 0 or 1 repetitions of the preceding pattern. |
# | `[]`      | Matches any character inside the brackets.  |
# | `{}`      | Matches a specific number of repetitions.   |
# | `|`       | Acts as an OR operator.                    |

# Example:
pattern = r'\d{3}-\d{3}-\d{4}'  # Matches a phone number format
text = 'My phone number is 123-456-7890.'
match = re.search(pattern, text)
print(match)  # Output: <re.Match object; span=(19, 31), match='123-456-7890'>


## 4. Escaping Special Characters
# If you want to use a special character as a literal (e.g., '.' or '*'), you need to escape it using a backslash (`\\`).

# Example:
pattern = r'\.'
text = 'This is a sentence.'
match = re.search(pattern, text)
print(match)  # Output: <re.Match object; span=(17, 18), match='.'>


## 5. Groups in Regular Expressions
# You can group patterns using parentheses `()` to capture parts of the match.

# Example:
pattern = r'(\d{3})-(\d{3})-(\d{4})'
text = '123-456-7890'
match = re.search(pattern, text)
if match:
    print(match.group(1))  # Output: 123
    print(match.group(2))  # Output: 456
    print(match.group(3))  # Output: 7890


## 6. Using `re.sub()` for Substitution
# You can use `re.sub()` to replace matches with a specified string.

# Example:
pattern = r'\d'
text = 'Phone: 123-456-7890'
new_text = re.sub(pattern, 'X', text)
print(new_text)  # Output: Phone: XXX-XXX-XXXX


# Solved Assignments

# Assignment 1: Write a regex to find all email addresses in a given string.

def find_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

# Example:
text = 'Please contact us at support@example.com and sales@company.org'
print(find_emails(text))  # Output: ['support@example.com', 'sales@company.org']


# Assignment 2: Write a regex to check if a string contains only letters and numbers.

def is_alphanumeric(text):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, text))

# Example:
text = 'Hello123'
print(is_alphanumeric(text))  # Output: True


# Assignment 3: Write a regex to validate a phone number in the format 123-456-7890.

def is_valid_phone_number(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

# Example:
phone = '123-456-7890'
print(is_valid_phone_number(phone))  # Output: True


# Assignment 4: Write a regex to extract the domain name from a URL.

def extract_domain(url):
    pattern = r'https?://(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(2)

# Example:
url = 'https://www.example.com'
print(extract_domain(url))  # Output: example.com


# Assignment 5: Write a regex to split a string by commas, ignoring commas inside quotes.

def split_by_commas(text):
    pattern = r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)'
    return re.split(pattern, text)

# Example:
text = 'one, "two, three", four'
print(split_by_commas(text))  # Output: ['one', '"two, three"', 'four']


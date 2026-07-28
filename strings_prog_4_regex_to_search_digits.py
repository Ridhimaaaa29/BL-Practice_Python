"""
PROG 4: To Use Regex To Search Digits
Regex to search digits: Write a regular expression to search digit inside a string

TESTCASE 1:

Input => Enter a string: fA7c33de85

Output =>

Digits found in the string: ['7', '3', '3', '8', '5']
TESTCASE 2:

Input => Enter a string: Engineer

Output =>

No digits found in the string.
Note => Try with different inputs
"""



# PROG 4: To Use Regex To Search Digits

import re

# Take input
text = input("Enter a string: ")

# Find all digits
digits = re.findall(r'\d', text)

# Display result
if digits:
    print("Digits found in the string:", digits)
else:
    print("No digits found in the string.")
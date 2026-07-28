"""
PROG 5: To Check Email Address
Regex to check valid email address

TESTCASE 1:

Input => Enter an email address: test@gmail.com

Output =>
test@gmail.com is a Valid Email Address.

TESTCASE 2:

Input => Enter an email address: test

Output =>
test is an Invalid Email Address.

TESTCASE 3:

Input => Enter an email address: test@

Output =>
test@ is an Invalid Email Address.

TESTCASE 4:

Input => Enter an email address: test@gmail

Output =>
test@gmail is an Invalid Email Address.

TESTCASE 5:

Input => Enter an email address: test@gmail.

Output =>
test@gmail. is an Invalid Email Address.

TESTCASE 6:

Input => Enter an email address: testgmail.com

Output =>
testgmail.com is an Invalid Email Address.

TESTCASE 7:

Input => Enter an email address: @yahoo.in

Output =>
@yahoo.in is an Invalid Email Address.
"""



# PROG 5: To Check Email Address

import re

# Take input
email = input("Enter an email address: ")

# Regular expression for email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Check if email is valid
if re.fullmatch(pattern, email):
    print(f"{email} is a Valid Email Address.")
else:
    print(f"{email} is an Invalid Email Address.")



    
"""
Explanation on RegEx :

A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings.

It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns
"""
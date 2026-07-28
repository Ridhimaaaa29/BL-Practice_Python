"""
PROG 5: Password Check
Develop a function which checks using regex whether the password is valid or not. Password policy says:
=> Password should be at least 8 Characters
=> It can not start with digit or special characters
=> It should have presence of at least 1 digit
=> It should have presence of atleast 1 symbol from from this set [‘@’, ‘#’, ‘$’, ‘%’, ‘^’, ‘&’ , ‘*’]
=> It should have both uppercase and lowercase letters \

TESTCASE 1:

Input => Enter your password: abcdef

Output =>
Password is invalid.

TESTCASE 2:

Input => Enter your password: abc123

Output =>
Password is invalid.

TESTCASE 3:

Input => Enter your password: #abc123456

Output =>
Password is invalid.

TESTCASE 4:

Input => Enter your password: 1abc123456

Output =>
Password is invalid.

TESTCASE 5:

Input => Enter your password: abcdefg%#

Output =>
Password is invalid.

TESTCASE 6:

Input => Enter your password: 12345678

Output =>
Password is invalid.

TESTCASE 7:

Input => Enter your password: #@$%^&*&^$

Output =>
Password is invalid.

TESTCASE 8:

Input => Enter your password: abc123@4#

Output =>
Password is invalid.

TESTCASE 9:

Input => Enter your password: ABCDE@1234

Output =>
Password is invalid.

TESTCASE 10:

Input => Enter your password: ABCde@1234

Output =>
Password is valid.

TESTCASE 11:

Input => Enter your password: A$c12345

Output =>
Password is valid.

TESTCASE 12:

Input => Enter your password: W0rld#567

Output =>
Password is valid.

Hint =>

Use RegEx
"""

# PROG 3: Remove Digits From The String

def remove_digits(text):
    result = ""
    digits = "0123456789"

    for ch in text:
        if ch not in digits:
            result += ch

    return result

text = input("Input String: ")
print("Output String without numbers:", remove_digits(text))
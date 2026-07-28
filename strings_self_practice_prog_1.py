"""
PROG 1: Full Name With Right Case Structure
Get the first name, middle name (if any) and last name of any of your close friends. Concatenate them together with a space character in between.

Refactor above program as a function, so that First Characters of First name, Middle name and Last name are upper cases and remaining characters are lower cases.

Function takes First Name, Middle Name and Last name as input arguments and returns the full name with right case structure.

Input =>
Enter your first name: farzana
Enter your middle name (if any, else press enter): f
Enter your last name: shaikh

Output => \

Formatted Full Name: Farzana F Shaikh
Hint =>

Use title()
Note => Try with different inputs
"""


# Function to format full name
def format_name(first, middle, last):
    first = first.title()
    middle = middle.title()
    last = last.title()

    if middle:
        return first + " " + middle + " " + last
    else:
        return first + " " + last


# Take input
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name (if any, else press enter): ")
last_name = input("Enter your last name: ")

# Call function
full_name = format_name(first_name, middle_name, last_name)

# Display output
print("\nFormatted Full Name:", full_name)

"""
Concepts Used:
def → Function definition
title() → Converts the first letter of each word to uppercase and the rest to lowercase.
if...else → Handles the case when no middle name is entered.
"""
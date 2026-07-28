"""
PROG 2 : Swap Case
Swap the case of each character in a string after removing leading and trailing white spaces:

Input => Input String: Is this a Good Example?

Output => Output String: iS THIS A gOOD eXAMPLE?

Note => Try with different inputs
"""


# Take input
text = input("Input String: ")

# Remove leading and trailing spaces
text = text.strip()

# Swap the case
result = text.swapcase()

# Display output
print("Output String:", result)


"""
Concepts Used:
strip() → Removes leading and trailing whitespace.
swapcase() → Converts uppercase letters to lowercase and lowercase letters to uppercase.
"""
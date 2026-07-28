"""
PROG 3: Counting Letters, Digits, and Special Symbols in a String

PROG 3.1: Counting Letters, Digits, and Special Symbols in a String Using Explicit Loops
Count all letters, digits, and special symbols from a given string

Input => Input String : P@#yn26at^&i5ve

Output =>

Number of letters: 8
Number of digits: 3
Number of special symbols: 4
Note => Try with different inputs
"""


# PROG 3.1: Counting Letters, Digits, and Special Symbols in a String Using Explicit Loops

# Take input
text = input("Input String : ")

letters = 0
digits = 0
special = 0

# Count using explicit loop
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

# Display result
print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of special symbols:", special)



"""
Explanation: \

In Python, the construct if __name__ == "__main__": is used to check whether a Python script is being run directly or if it is being imported as a module into another script.

__name__ is a special built-in variable in Python. When a script is executed, Python assigns the name "__main__" to the __name__ variable.
When the script is imported as a module, __name__ is set to the module's name instead of "__main__".
"""
"""
PROG 3: Remove Digits From The String
Removal numbers from a string : Develop a function that takes a string as an input argument and returns a string without any numbers.

Input => Input String: abcd1234

Output => Output String without numbers: abcd

Hint =>

Use membership operator
Note => Try with different inputs
"""


# PROG 3: Remove Digits From The String

# Function to remove digits
def remove_digits(text):
    result = ""

    for ch in text:
        if ch not in "0123456789":
            result += ch

    return result


# Take input
text = input("Input String: ")

# Call function
output = remove_digits(text)

# Display output
print("Output String without numbers:", output)


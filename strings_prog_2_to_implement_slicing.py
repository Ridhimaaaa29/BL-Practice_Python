"""
PROG 2: To Implement Slicing
New string from selected characters: Create a new string made of the first, middle, and last characters of each input string.

Input => Input string: 'Knowledge'

Output =>

Output string containing first , middle and last character: 'Kle'
Hint =>

Plan using slice operator to get middle character
Note => Try with different inputs
"""

# PROG 2: To Implement Slicing

# Take input
string = input("Input string: ")

# Find first, middle and last characters
first = string[0]
middle = string[len(string) // 2]
last = string[-1]

# Create new string
result = first + middle + last

# Display output
print("Output string containing first, middle and last character:", result)
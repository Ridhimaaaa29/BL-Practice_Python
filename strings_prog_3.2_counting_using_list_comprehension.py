"""
PROG 3.2: Counting Letters, Digits, and Special Symbols in a String Using List Comprehension
Note => Try with different inputs \

Input => Input String : P@#yn26at^&i5ve

Output =>

Number of letters: 8
Number of digits: 3
Number of special symbols: 4
"""


# PROG 3.2: Counting Letters, Digits, and Special Symbols in a String Using List Comprehension

# Take input
text = input("Input String: ")

# Using list comprehensions
letters = [ch for ch in text if ch.isalpha()]
digits = [ch for ch in text if ch.isdigit()]
special = [ch for ch in text if not ch.isalpha() and not ch.isdigit()]

# Display result
print("Number of letters:", len(letters))
print("Number of digits:", len(digits))
print("Number of special symbols:", len(special))



"""
List Comprehension: \

List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing sequence (like a list, tuple, or range), optionally filtering items with a condition.

[expression for item in iterable if condition]

Explanation:
=> expression: The value or operation to apply to each item.
=> item: The variable representing each element in the iterable.
=> iterable: The sequence of elements to iterate over (e.g., a list, range).
=> condition (optional): A filter that determines if the item should be included in the new list.
"""
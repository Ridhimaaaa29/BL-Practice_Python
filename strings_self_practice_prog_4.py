"""
PROG 4: Count Character In The String
Character Counter: Develop a program which counts occurrences of all alphanumeric characters in s string. All characters are converted to lower case first

Input => Input String: An Apple.

Output =>

Character Counts: {'a': 2, 'n': 1, 'p': 2, 'l': 1, 'e': 1}
Note => Try with different inputs
"""

# PROG 4: Count Character In The String

# Take input
text = input("Input String: ")

# Convert to lowercase
text = text.lower()

# Dictionary to store character counts
char_count = {}

# Count only alphanumeric characters
for ch in text:
    if ch.isalnum():
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

# Display result
print("Character Counts:", char_count)

"""
lower() → Converts all characters to lowercase.
isalnum() → Checks whether a character is a letter or digit.
Dictionary ({}) → Stores the frequency of each character.
in operator → Checks whether a key already exists in the dictionary.
"""
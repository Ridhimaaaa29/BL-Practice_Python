"""
PROG 1: Creating a Tuple of Squares and Accessing Specific Elements
=> Create a tuple of squares of all numbers between 0 to 9.
=> Print the 3rd , 5th and 7th elements of this sequence. Also print the first 3 elements of this tuple.
=> Plan using tuple constructor and list comprehension for solving this.

Key learnings:

List comprehension
Tuple constructor : tuple()
Use of index for accessing elements in tuple
Use of slicing as list
Discuss when to use tuple constructor and tuple literal
**Input =>**None

Output => \

The List of Square of Numbers is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Use of index for accessing elements in tuple
3rd element: 4
5th element: 16
7th element: 36
First 3 elements: (0, 1, 4)
"""

# Create a list of squares using list comprehension
square_list = [num ** 2 for num in range(10)]

# Convert the list into a tuple using tuple() constructor
square_tuple = tuple(square_list)

# Display the list
print("The List of Square of Numbers is", square_list)

print("Use of index for accessing elements in tuple")

# Access specific elements using indexing
print("3rd element:", square_tuple[2])
print("5th element:", square_tuple[4])
print("7th element:", square_tuple[6])

# Access first three elements using slicing
print("First 3 elements:", square_tuple[:3])


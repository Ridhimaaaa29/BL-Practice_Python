"""
What is a list in Python?
A list in Python is a built-in data structure that allows you to store a collection of items in a single variable.
Lists are ordered, mutable (meaning you can change their content), and can contain elements of different data types, including other lists.

Why do we prefer lists over arrays?
We prefer lists over arrays in Python for several reasons:
They are more flexible and can hold elements of different data types, while arrays typically require all elements to be of the same type.
Lists have built-in methods that make it easy to manipulate and manage the data they contain, such
Lists are dynamic in size, meaning they can grow and shrink as needed, while arrays have a fixed size.
"""

# List operations with examples

# Functions for adding 
# 1. append() - Adds an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# 2. insert() - Inserts an element at a specified index
my_list.insert(1, 1.5)      
print(my_list)  # Output: [1, 1.5, 2, 3, 4]

# 3. extend() - Extends the list by appending elements from another iterable
my_list.extend([5, 6])  
print(my_list)  # Output: [1, 1.5, 2, 3, 4, 5, 6]   

# Functions for removing
# 1. remove() - Removes the first occurrence of a specified value
my_list.remove(1.5)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 2. pop() - Removes and returns the element at a specified index (default is the last element)
popped_element = my_list.pop(2)
print(popped_element)  # Output: 3
print(my_list)  # Output: [1, 2, 4, 5, 6]

# 3. clear() - Removes all elements from the list
my_list.clear()
print(my_list)  # Output: []

# Functions for searching and sorting
# 1. sort() - Sorts the list in ascending order
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]

# 2. reverse() - Reverses the order of the list
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

# 3. count() - Returns the number of occurrences of a specified value
my_list = [1, 2, 2, 3, 4, 2]
count_of_twos = my_list.count(2)
print(count_of_twos)  # Output: 3

# 4. index() - Returns the index of the first occurrence of a specified value
index_of_three = my_list.index(3)
print(index_of_three)  # Output: 3

# 5. len() - Returns the number of elements in the list
length_of_list = len(my_list)
print(length_of_list)  # Output: 6

# comprehensions - A concise way to create lists
# Example: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

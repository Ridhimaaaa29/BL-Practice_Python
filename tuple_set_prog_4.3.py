"""
PROG 4.3: Using the intersection() Method
Input =>
School Friends: ['John', 'Alice', 'Bob', 'David']
College Friends: ['Alice', 'Charlie', 'David', 'Eve']

Output =>

Common friends (Set intersection method): ['David', 'Alice']
b = 5
Note => Try with different user inputs
"""

# Create lists
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find common friends using the intersection() method
common_friends = list(set(school_friends).intersection(college_friends))

# Display common friends
print("\nCommon friends (Set intersection method):", common_friends)

"""
Explanation :

Difference between & Operator and intersection() Method:

The & Operator: Both operands must be sets.
The intersection() Method: The method can take any iterable, such as lists, making it more flexible.
"""
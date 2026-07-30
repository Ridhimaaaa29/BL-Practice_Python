# PROG 5: Employee Access Rights Update Based on Current Staff

"""
PROG 5: Creating a List of All Unique Friends Using Set Union Operations
=> All Friends: From the above friends’ lists, plan creating list of all friends

Note:
Solve using | operator of set and union method of set.

Key Learnings for above two:
Use of set intersection and union methods
"""


"""
PROG 5.1: Using the | Operator
Input =>
School Friends: ['John', 'Alice', 'Bob', 'David']
College Friends: ['Alice', 'Charlie', 'David', 'Eve']

Output =>

All friends (Set | operator): ['David', 'Eve', 'Alice', 'John', 'Bob', 'Charlie']
Note => Try with different user inputs
"""



# PROG 5.1: Using the | Operator

# Create lists
school_friends = ["John", "Alice", "Bob", "David"]
college_friends = ["Alice", "Charlie", "David", "Eve"]

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find all unique friends using | operator
all_friends = set(school_friends) | set(college_friends)

# Display result
print("\nAll friends (Set | operator):", list(all_friends))
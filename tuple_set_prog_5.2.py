"""
PROG 5.2: Using the union() Method
Input =>
School Friends: ['John', 'Alice', 'Bob', 'David']
College Friends: ['Alice', 'Charlie', 'David', 'Eve']

Output =>

All friends (Set union method): ['David', 'Eve', 'Alice', 'John', 'Bob', 'Charlie']
Note => Try with different user inputs
"""

# PROG 5.2: Using the union() Method

# Create lists
school_friends = ["John", "Alice", "Bob", "David"]
college_friends = ["Alice", "Charlie", "David", "Eve"]

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find all unique friends using union() method
all_friends = set(school_friends).union(college_friends)

# Display result
print("\nAll friends (Set union method):", list(all_friends))
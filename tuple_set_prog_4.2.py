"""
PROG 4.2: Using the & Operator
Input =>
School Friends: ['John', 'Alice', 'Bob', 'David']
College Friends: ['Alice', 'Charlie', 'David', 'Eve']

Output =>

Common friends (Set & operator): ['David', 'Alice']
Note => Try with different user inputs
"""

# Create lists
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

#Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Convert lists to sets and find common friends using & operator
common_friends = list(set(school_friends) & set(college_friends))

# Display result
print("\nCommon friends (Set & operator):", common_friends)
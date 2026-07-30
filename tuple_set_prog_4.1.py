"""
PROG 4: Finding Common Elements Between Two Lists Using Iteration, Set Operations, and Set Intersection Method
=> Create a list of your college friends and school friends.
=> From these two lists, create a list of common friends who are both school and college friends.

Note :

First solve this problem using iterating over these two lists .
Then solve using & operator for sets.
Also demonstrate using the intersection() method of set.
Also demonstrate the difference between & operator and intersection method
"""

"""
PROG 4.1: Using Iteration: Manually finding common friends by iterating over two lists.
Input =>
School Friends: ['John', 'Alice', 'Bob', 'David']
College Friends: ['Alice', 'Charlie', 'David', 'Eve']

Output =>

Common friends (Iterative method): ['Alice', 'David']
Note => Try with different user inputs
"""

# Create lists
school_friends = ['John', 'Alice', 'Bob', 'David']
college_friends = ['Alice', 'Charlie', 'David', 'Eve']

# Display lists
print("School Friends:", school_friends)
print("College Friends:", college_friends)

# Find common friends using iteration
common_friends = []
for friend in school_friends:
    if friend in college_friends:
        common_friends.append(friend)

# Display common friends
print("\nCommon friends (Iterative method):", common_friends)
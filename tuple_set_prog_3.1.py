"""
PROG 3: Swapping Variables Using Traditional and Pythonic Methods
=> Develop a python program to swap two variables.

=> For example if a = 5 and b = 10, then after swapping a becomes 10 and b holds a value of 5.

Hint :
Develop this program in first traditional way using 3rd variable and in pythonic way

Key Learning:

Packing and Unpacking of Tuple
Also share how python supports return of more than one variable
"""


"""
PROG 3.1: Swapping Variables Using Traditional Method
Input =>
Enter the value of a: 5
Enter the value of b: 10

Output =>

Initial Value of a & b are
a = 5
b = 10
After traditional swapping:
a = 10
b = 5
Note => Try with different user inputs
"""

# Take input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Display initial values
print("\nInitial Value of a & b are")
print("a: ", a)
print("b: ", b)

# Traditional swapping using a temporary variable
temp = a
a = b
b = temp

# Display values after swapping
print("\nAfter traditional swapping:")
print("a = ", a)
print("b = ", b)
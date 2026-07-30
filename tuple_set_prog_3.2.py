"""
PROG 3.2: Swapping Variables Using Pythonic Method
Input =>
Enter the value of a: 5
Enter the value of b: 10

Output =>

Initial Value of a & b are
a = 5
b = 10
After pythonic swapping:
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

# Pythonic swapping using tuple packing and unpacking
a, b = b, a

# Display values after swapping
print("\nAfter pythonic swapping:")
print("a = ", a)
print("b = ", b)


"""
Explanation:

Pythonic Method:
Python allows direct swapping of variables using
tuple packing and unpacking (a, b = b, a), eliminating 
the need for a third variable.
"""
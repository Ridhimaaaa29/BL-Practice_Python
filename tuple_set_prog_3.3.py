"""
PROG 3.3: Swapping Variables Using Tuple Packing and Unpacking
Input =>
Enter the value of a: 5
Enter the value of b: 10

Output =>

Initial Value of a & b are
a = 5
b = 10

After swapping (using function):
x = 10
y = 5
Note => Try with different user inputs
"""

def swap_values(x, y):
    """
    Function to swap two values using tuple packing and unpacking.
    
    Parameters:
    x (int): First value
    y (int): Second value
    
    Returns:
    tuple: Swapped values (y, x)
    """
    return y, x

# Take input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Display initial values
print("\nInitial Value of a & b are")
print("a = ", a)
print("b = ", b)

# Call the swap function
x, y = swap_values(a, b)

# Display values after swapping
print("\nAfter swapping (using function):")
print("x = ", x)
print("y = ", y)


"""
Explanation:

Returning Multiple Values: Python allows functions to return 
multiple values using tuples.
"""


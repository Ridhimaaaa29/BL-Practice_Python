"""
PROG 2: Comparing the Size and Creation Time of List vs. Tuple
=> Create a tuple of 10 integer numbers and also a list of the same 10 numbers.
=> Using getsizeof() method from sys library/module check the size of list and tuple.
=> Using timeit() method from timeit module/library - check the creation

Key Learnings :

Tuple takes less size as well as less creation time than that of a list.
Thus fixed size sequence which is unlikely to change during program, one should tuple instead of list.
For example database record
Using getsizeof() method
Using timeit() method
Input => None

Output =>

Size of tuple: 120 bytes
Size of list: 136 bytes
Creation time for tuple (in seconds): 0.08818072700000812
Creation time for list (in seconds): 0.13332087799994952
Hint =>

Use sys.getsizeof()
Use timeit.timeit()
"""


import sys
import timeit

# Create a tuple and a list
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Check memory size
print("Size of tuple:", sys.getsizeof(numbers_tuple), "bytes")
print("Size of list:", sys.getsizeof(numbers_list), "bytes")

# Measure creation time
tuple_time = timeit.timeit(
    stmt="(1,2,3,4,5,6,7,8,9,10)",
    number=1000000
)

list_time = timeit.timeit(
    stmt="[1,2,3,4,5,6,7,8,9,10]",
    number=1000000
)

# Display creation time
print("Creation time for tuple (in seconds):", tuple_time)
print("Creation time for list (in seconds):", list_time)
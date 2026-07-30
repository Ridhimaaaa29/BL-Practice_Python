"""
PROG 5: Employee Access Rights Update Based on Current Staff
=> A MIS person maintains a list of employees with access rights and another list representing the current employees.
=> Every month, few of the employees may move out and the current employees list gets updated on that day.
=> As a MIS person you would like to update the access list based on the current employees list.
=> Create a program to do this.

Input =>
Enter the employees with access rights (comma-separated): Alice, Bob, Charlie, David
Enter the current employees (comma-separated): bob, David, Emily

Output => \

Updated Access Rights List:
David
Bob
Hint =>
=> Use the intersection_update() method of a set.
"""


# PROG 5: Employee Access Rights Update Based on Current Staff

# Take input
access_rights = input("Enter the employees with access rights (comma-separated): ")
current_employees = input("Enter the current employees (comma-separated): ")

# Convert input into sets (case-insensitive)
access_set = {employee.strip().lower() for employee in access_rights.split(",")}
current_set = {employee.strip().lower() for employee in current_employees.split(",")}

# Update access rights using intersection_update()
access_set.intersection_update(current_set)

# Display updated access rights
print("\nUpdated Access Rights List:")

for employee in access_set:
    print(employee.title())
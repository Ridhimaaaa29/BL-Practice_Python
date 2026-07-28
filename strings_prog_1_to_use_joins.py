"""
A String is a data structure in Python Programming that represents a sequence of characters.
It is an immutable data type, meaning that once you have created a string, you cannot change it.
Python String are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.
"""

# PROG 1: To Use Join
"""
Placenames: Enter names of 5 places you would like to visit, keep them in a list.

While taking the input prompt the user to place the number (1 to 5) to be entered as well. Print these places with uppercase letters.

Also create a new string having all these 5 place names separated by comma and space between two places.

Input =>
Enter the name of place 1: bengaluru
Enter the name of place 2: mumbai
Enter the name of place 3: goa
Enter the name of place 4: pune
Enter the name of place 5: mysore

Output => \

Places stored in list: ['bengaluru', 'mumbai', 'goa', 'pune ', 'mysore']

All places separated by comma and space and in uppercase: BENGALURU, MUMBAI, GOA, PUNE , MYSORE
Hint =>

Use join()
Use upper()
"""

places = []

# Take input for 5 places
for i in range(1, 6):
    place = input(f"Enter the name of place {i}: ")
    places.append(place)

# Display the list
print("\nPlaces stored in list:", places)

# Convert each place to uppercase
upper_places = []
for place in places:
    upper_places.append(place.upper())

# Join the place names with comma and space
result = ", ".join(upper_places)

print("\nAll places separated by comma and space and in uppercase:", result)
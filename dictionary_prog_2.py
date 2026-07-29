"""
PROG 2: Update The Dictionary
=> Additional information on address: Later his email id and phone numbers are received as another dictionary.
=> Develop a code to merge these 2 dictionaries.
=> Print the keys, values and items using methods keys(), values() and items().

Hint :
=> Plan doing this by using update() method, ** unpacking **, | union operator and |= operator.
=> Try understanding what should be preferred way for Python 3.9 and above
=> Also understand when to use | and when to use |=

Input => None

Output =>

Merged Dictionary using update():

Using Keys Method: dict_keys(['Name', 'City of Stay', 'Pincode', 'Email', 'Phone'])
Using Values Method: dict_values(['John Doe', 'Mumbai', '400088', 'john.doe@example.com', '1234567890'])
Using Items Method: dict_items([('Name', 'John Doe'), ('City of Stay', 'Mumbai'), ('Pincode', '400088'), ('Email', 'john.doe@example.com'), ('Phone', '1234567890')])


Merged Dictionary using unpacking (**):

Using Keys Method: dict_keys(['Name', 'City of Stay', 'Pincode', 'Email', 'Phone'])
Using Values Method: dict_values(['John Doe', 'Mumbai', '400088', 'john.doe@example.com', '1234567890'])
Using Items Method: dict_items([('Name', 'John Doe'), ('City of Stay', 'Mumbai'), ('Pincode', '400088'), ('Email', 'john.doe@example.com'), ('Phone', '1234567890')])


Merged Dictionary using | operator:

Using Keys Method: dict_keys(['Name', 'City of Stay', 'Pincode', 'Email', 'Phone'])
Using Values Method: dict_values(['John Doe', 'Mumbai', '400088', 'john.doe@example.com', '1234567890'])
Using Items Method: dict_items([('Name', 'John Doe'), ('City of Stay', 'Mumbai'), ('Pincode', '400088'), ('Email', 'john.doe@example.com'), ('Phone', '1234567890')])


Merged Dictionary using |= operator:

Using Keys Method: dict_keys(['Name', 'City of Stay', 'Pincode', 'Email', 'Phone'])
Using Values Method: dict_values(['John Doe', 'Mumbai', '400088', 'john.doe@example.com', '1234567890'])
Using Items Method: dict_items([('Name', 'John Doe'), ('City of Stay', 'Mumbai'), ('Pincode', '400088'), ('Email', 'john.doe@example.com'), ('Phone', '1234567890')])
Hint =>

Use copy()
Use update()
Use keys()
Use values()
Use items()

"""


# First dictionary
friend_details = {
    "Name": "Adi",
    "City of Stay": "Chandigarh",
    "Pincode": "160017"
}

# Second dictionary
additional_details = {
    "Email": "adi@gmail.com",
    "Phone": "1234567890"
}

# Using update() 
dict1 = friend_details.copy()
dict1.update(additional_details)

print("Merged Dictionary using update():\n")
print("Using Keys Method:", dict1.keys())
print("Using Values Method:", dict1.values())
print("Using Items Method:", dict1.items())

# Using unpacking (**) 
dict2 = {**friend_details, **additional_details}

print("\n\nMerged Dictionary using unpacking (**):\n")
print("Using Keys Method:", dict2.keys())
print("Using Values Method:", dict2.values())
print("Using Items Method:", dict2.items())

# Using | operator
dict3 = friend_details | additional_details

print("\n\nMerged Dictionary using | operator:\n")
print("Using Keys Method:", dict3.keys())
print("Using Values Method:", dict3.values())
print("Using Items Method:", dict3.items())

# Using |= operator 
dict4 = friend_details.copy()
dict4 |= additional_details

print("\n\nMerged Dictionary using |= operator:\n")
print("Using Keys Method:", dict4.keys())
print("Using Values Method:", dict4.values())
print("Using Items Method:", dict4.items())
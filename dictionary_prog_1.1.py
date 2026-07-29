# PROG 1: Add Data In Dictionary

"""
PROG 1.1: Add Data In Dictionary With Hard-Coded Values
=> Friends Details: For one of your close friends, please take the details of Name, City of Stay, Pincode,. Keep them in a dictionary and print them one by one. Also print its type and check.

=>Try printing this with both over keys and also with keys and values using method items.

**Input =>**None

Output => \

Type of friend_details: <class 'dict'>

Printing details using keys:
Name: Ridhima
City of Stay: Gurgaon
Pincode: 122001

Printing details using items():
Name: Ridhima
City of Stay: Gurgaon
Pincode: 122001

Hint =>

Use items()
"""


# Hard-coded dictionary
friend_details = {
    "Name": "Ridhima",
    "City of Stay": "Gurgaon",
    "Pincode": 122001
}

# Print type
print("Type of friend_details:", type(friend_details))

# Print using keys
print("\nPrinting details using keys:")
for key in friend_details:
    print(f"{key}: {friend_details[key]}")
# explanation: In the above code, we are iterating over the keys of the dictionary and printing the key along with its corresponding value.

# Print using items()
print("\nPrinting details using items():")
for key, value in friend_details.items():
    print(f"{key}: {value}")



"""
PROG 1.2: Add Data In Dictionary With User Input

Input =>
Enter your name: Aadhya
Enter your city of stay: Amritsar
Enter your pincode: 143001

Output =>
Type of user_details_dict: <class 'dict'>

Printing details using keys:
Name: AAadhya
City of Stay: Amritsar
Pincode: 143001

Printing details using items():
Name: Aadhya
City of Stay: Amritsar
Pincode: 143001

"""


# Take user input
name = input("Enter your name: ")
city = input("Enter your city of stay: ")
pincode = input("Enter your pincode: ")

# Store data in dictionary
friend_details = {
    "Name": name,
    "City of Stay": city,
    "Pincode": pincode
}

# Print type
print("\nType of friend_details:", type(friend_details))

# Print using keys
print("\nPrinting details using keys:")
for key in friend_details:
    print(f"{key}: {friend_details[key]}")

# Print using items()
print("\nPrinting details using items():")
for key, value in friend_details.items():
    print(f"{key}: {value}")
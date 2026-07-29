"""
PROG 4: Dynamic Dictionary Update with User Input for Friend Type Selection
=> In the above dictionary - plan adding “Country” as “India” as default value, “Friend-Type” as another key.
=> Possible values of Friend Type can be [“School”, “College”, “Neighbourhood”].
=> Initially do not add any value for “FriendType”
=> Print and see how the dictionary changes.
=> Define “Friend Type” based on one of the above options.
=> Print and check.

Input =>

Dictionary after adding default values:

Keys: dict_keys(['Name', 'City of Stay', 'Pincode', 'Country', 'Friend-Type'])
Values: dict_values(['John Doe', 'Mumbai', '400088', 'India', ''])
Items: dict_items([('Name', 'John Doe'), ('City of Stay', 'Mumbai'), ('Pincode', '400088'), ('Country', 'India'), ('Friend-Type', '')])

Select Friend Type:
1. School
2. College
3. Neighbourhood
Enter the number corresponding to the Friend Type: 2
Output =>

Dictionary after setting 'Friend-Type':

Keys: dict_keys(['Name', 'City of Stay', 'Pincode', 'Country', 'Friend-Type'])
Values: dict_values(['John Doe', 'Mumbai', '400088', 'India', 'College'])
Items: dict_items([('Name', 'John Doe'), ('City of Stay', 'Mumbai'), ('Pincode', '400088'), ('Country', 'India'), ('Friend-Type', 'College')])
Hint =>

Use setdefault() function for the above
Note => Try with different inputs
"""



# Friend details dictionary
friend_details = {
    "Name": "John Doe",
    "City of Stay": "Mumbai",
    "Pincode": "400088"
}

# Add default values using setdefault()
friend_details.setdefault("Country", "India")
friend_details.setdefault("Friend-Type", "")

# Display dictionary after adding default values
print("Dictionary after adding default values:\n")

print("Keys:", friend_details.keys())
print("Values:", friend_details.values())
print("Items:", friend_details.items())

# Friend type options
print("\nSelect Friend Type:")
print("1. School")
print("2. College")
print("3. Neighbourhood")

choice = input("Enter the number corresponding to the Friend Type: ")

# Update Friend-Type based on user choice
if choice == "1":
    friend_details["Friend-Type"] = "School"
elif choice == "2":
    friend_details["Friend-Type"] = "College"
elif choice == "3":
    friend_details["Friend-Type"] = "Neighbourhood"
else:
    print("Invalid choice!")

# Display updated dictionary
print("\nDictionary after setting 'Friend-Type':\n")

print("Keys:", friend_details.keys())
print("Values:", friend_details.values())
print("Items:", friend_details.items())
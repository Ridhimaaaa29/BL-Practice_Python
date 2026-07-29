"""
PROG 3.1: To Remove Data From Dictionary Using del
=> Lastly it was decided to remove the pincode from the merged dictionary only and note from the first dictionary.
=> Refactor merge operation needed.

Input => None
Output =>

Merged Dictionary after removing pincode using del:
{'Name': 'Franz Kafka', 'City of Stay': 'Prague', 'Email': 'franz.kafka@example.com', 'Phone': '123-456-7890'}
Note => Try with different user inputs
"""

"""
PROG 3.1: To Remove Data From Dictionary Using del
=> Lastly it was decided to remove the pincode from the merged dictionary only and note from the first dictionary.
=> Refactor merge operation needed.

Input => None
Output =>

Merged Dictionary after removing pincode using del:
{'Name': 'Franz Kafka', 'City of Stay': 'Prague', 'Email': 'franz.kafka@example.com', 'Phone': '123-456-7890'}
Note => Try with different user inputs
"""

# PROG 3.1: To Remove Data From Dictionary Using del

# First dictionary
friend_details = {
    "Name": "Franz Kafka",
    "City of Stay": "Prague",
    "Pincode": "110001"
}

# Second dictionary
additional_details = {
    "Email": "franz.kafka@example.com",
    "Phone": "123-456-7890"
}

# Merge the dictionaries
merged_dictionary = friend_details.copy()
merged_dictionary.update(additional_details)

# Remove pincode only from the merged dictionary
del merged_dictionary["Pincode"]

# Display the result
print("Merged Dictionary after removing pincode using del:")
print(merged_dictionary)
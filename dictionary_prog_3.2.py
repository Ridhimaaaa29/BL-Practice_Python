"""
PROG 3.2: To Remove Data From Dictionary Using pop
=> Lastly it was decided to remove the pincode from the merged dictionary only and note from the first dictionary.
=> Refactor merge operation needed.

Input => None
Output =>

Merged Dictionary after removing pincode using pop:
{'Name': 'Franz Kafka', 'City of Stay': 'Prague', 'Email': 'franz.kafka@example.com', 'Phone': '123-456-7890'}
Note => Try with different user inputs"""



# Friend's details dictionary
friend_details = {
    "Name": "Franz Kafka",
    "City of Stay": "Prague",
    "Pincode": "10001"
}

# Additional information dictionary
additional_info = {
    "Email": "franz.kafka@example.com",
    "Phone": "123-456-7890"
}

# Merge dictionaries
merged_dict = {**friend_details, **additional_info}

# Remove pincode from the merged dictionary
merged_dict.pop("Pincode")

# Display the result
print("Merged Dictionary after removing pincode using pop:")
print(merged_dict)
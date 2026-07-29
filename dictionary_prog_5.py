"""
PROG 5: To Search The Data In Dictionary
=> List of Friends’ details: Create similar details for five(5) of your friends, with following changes.

=> Friend name becomes the key and value is a list having address details and contact details.

=> Address detail is a dictionary having keys as “City” and “Pincode”. Contact details is another dictionary having “email-id” and “PhoneNumber”.

=> Based on user input, print any friend’s any details like “City”, “Pincode”, “email-id” or “PhoneNumber”

TESTCASE 1:

Input =>
Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): Friend5
Enter detail type (City/Pincode/Email/PhoneNumber): Pincode

Output =>
Friend5's Pincode: 33101

TESTCASE 2:

Input =>
Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): Friend2
Enter detail type (City/Pincode/Email/PhoneNumber): City

Output =>
Friend2's City: Los Angeles.

TESTCASE 3:

Input =>
Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): Friend4
Enter detail type (City/Pincode/Email/PhoneNumber): Email

Output =>
Friend4's Email: friend4@example.com

TESTCASE 4:

Input =>
Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): Friend1
Enter detail type (City/Pincode/Email/PhoneNumber): PhoneNumber

Output =>
Friend1's PhoneNumber: 1234567890

TESTCASE 5:

Input =>
Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): abc
Enter detail type (City/Pincode/Email/PhoneNumber): City

Output =>
Friend not found!

TESTCASE 6:

Input =>
Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): Friend4
Enter detail type (City/Pincode/Email/PhoneNumber): xyz

Output =>
Invalid detail type!

Note => Try with different user inputs
"""


# PROG 5: To Search The Data In Dictionary

friends = {
    "Friend1": [
        {"City": "New York", "Pincode": "10001"},
        {"Email": "friend1@example.com", "PhoneNumber": "1234567890"}
    ],
    "Friend2": [
        {"City": "Los Angeles", "Pincode": "90001"},
        {"Email": "friend2@example.com", "PhoneNumber": "2345678901"}
    ],
    "Friend3": [
        {"City": "Chicago", "Pincode": "60601"},
        {"Email": "friend3@example.com", "PhoneNumber": "3456789012"}
    ],
    "Friend4": [
        {"City": "Houston", "Pincode": "77001"},
        {"Email": "friend4@example.com", "PhoneNumber": "4567890123"}
    ],
    "Friend5": [
        {"City": "Miami", "Pincode": "33101"},
        {"Email": "friend5@example.com", "PhoneNumber": "5678901234"}
    ]
}

# User Input
friend_name = input("Enter friend's name (Friend1/Friend2/Friend3/Friend4/Friend5): ")
detail = input("Enter detail type (City/Pincode/Email/PhoneNumber): ")

# Search
if friend_name in friends:

    address = friends[friend_name][0]
    contact = friends[friend_name][1]

    if detail == "City":
        print(f"{friend_name}'s City:", address["City"])

    elif detail == "Pincode":
        print(f"{friend_name}'s Pincode:", address["Pincode"])

    elif detail == "Email":
        print(f"{friend_name}'s Email:", contact["Email"])

    elif detail == "PhoneNumber":
        print(f"{friend_name}'s PhoneNumber:", contact["PhoneNumber"])

    else:
        print("Invalid detail type!")

else:
    print("Friend not found!")
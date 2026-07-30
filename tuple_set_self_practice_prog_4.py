"""
PROG 4 : Email Marketing Duplicate Checker for Subscribers and New Sign-ups
=> A marketing manager has two email lists - one for current subscribers and another for new sign-ups.
=> Since the data is old, among the new sign-ups, there is a possibility that some of the new sign up members are already present in the current subscribers list.
=> Marketing manager wants a software solution to check whether any such email ids exist or not and if yes, share the email ids.
=> To help the marketing manager - plan developing a program.

TESTCASE 1:

Input =>
Enter the current subscribers' emails (comma-separated): alice@example.com, john@example.com, bob@example.com
Enter the new sign-ups' emails (comma-separated): john@example.com, mary@example.com, david@example.com

Output =>
The following email addresses are present in both lists: john@example.com

TESTCASE 2:

Input =>
Enter the current subscribers' emails (comma-separated): alice@example.com, john@example.com, bob@example.com
Enter the new sign-ups' emails (comma-separated): mary@example.com, david@example.com

Output =>
There are no common email addresses between current subscribers and new sign-ups.

Hint =>
=> Use the isdisjoint() method check if sets has a common elements
=> If above condition is true then use the intersection() method to display common elements
"""


# PROG 4: Email Marketing Duplicate Checker for Subscribers and New Sign-ups

# Take input
current_emails = input("Enter the current subscribers' emails (comma-separated): ")
new_emails = input("Enter the new sign-ups' emails (comma-separated): ")

# Convert input into sets
current_set = {email.strip().lower() for email in current_emails.split(",")}
new_set = {email.strip().lower() for email in new_emails.split(",")}

# Check for common email addresses
if current_set.isdisjoint(new_set):
    print("There are no common email addresses between current subscribers and new sign-ups.")
else:
    common_emails = current_set.intersection(new_set)

    print("The following email addresses are present in both lists:")
    for email in common_emails:
        print(email)
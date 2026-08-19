"""
This module implements the Binary Search algorithm  to search for a treasure ID in a sorted
list of treasure IDs.

This program will return the index of the treasure if it is found and if it does not exist,
it will return -1.

Binary Search is used because the treasure IDs are already maintained in sorted order
"""

def binary_search(treasures, target):
    """
    treasures: sorted list of treasure IDs
    target: treasure ID entered by the player
    """

    # Define the search range for the sorted treasure list.
    low = 0
    high = len(treasures) - 1

    # Keep searching until the range is valid.
    while low <= high:

        # Find the middle position of the current search range.
        mid = (low + high) // 2

        # If the middle value is the target, return its index immediately.
        if treasures[mid] == target:
            return mid

        # If the target is larger, move the left boundary to the right half.
        elif treasures[mid] < target:
            low = mid + 1

        # If the target is smaller, move the right boundary to the left half.
        else:
            high = mid - 1

    # The target does not exist in the list.
    return -1
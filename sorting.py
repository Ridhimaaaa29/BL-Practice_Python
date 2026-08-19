"""
This module contains the four sorting algorithms required
for arranging the players in ascending order
of their scores in the Algorithm Arena game project:

1. Selection Sort
2. Bubble Sort
3. Merge Sort
4. Quick Sort

Player format:
    ("Player Name", score)

Example:
    ("Arjun", 450)
"""

# 1. SELECTION SORT

def selection_sort(players):
    """
    Selection Sort repeatedly finds the player with the
    smallest score from the unsorted portion and places
    that player at the correct position.

    Time Complexity:
        Best Case:    O(n^2)
        Average Case: O(n^2)
        Worst Case:   O(n^2)

    Space Complexity:
        O(1) auxiliary space
    """

    # Creating a copy so that the original player list is not modified.
    players = players.copy()
    n = len(players)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if players[j][1] < players[min_index][1]:
                min_index = j

        players[i], players[min_index] = (
            players[min_index],
            players[i]
        )

    return players

# 2. BUBBLE SORT

def bubble_sort(players):
    """
    Bubble Sort repeatedly compares adjacent players.
    If they are in the wrong order, they are swapped.

    After every pass, the largest remaining score
    moves towards the end of the list.

    Time Complexity:
        Best Case:    O(n)
        Average Case: O(n^2)
        Worst Case:   O(n^2)

    Space Complexity:
        O(1) auxiliary space
    """

    players = players.copy()
    n = len(players)

    for i in range(n):
        # Used to detect whether any swapping occurred.
        swapped = False
        # Compare adjacent elements. The last i elements are already sorted.
        for j in range(n - i - 1):
            if players[j][1] > players[j + 1][1]:
                # Swap the two players.
                players[j], players[j + 1] = (
                    players[j + 1],
                    players[j]
                )
                swapped = True
        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break
    return players

# 3. MERGE SORT

def merge_sort(players):
    """
    Merge Sort uses the Divide and Conquer technique.

    The list is repeatedly divided into smaller lists.
    These smaller lists are then merged in sorted order.

    Time Complexity:
        Best Case:    O(n log n)
        Average Case: O(n log n)
        Worst Case:   O(n log n)

    Space Complexity:
        O(n)
    """

    # A list containing zero or one element is already sorted.
    if len(players) <= 1:
        return players

    # Find the middle position to split the list into two halves.
    mid = len(players) // 2

    # Divide the list into left and right sections.
    left = players[:mid]
    right = players[mid:]

    # Sort both halves recursively before merging them.
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves back into one ordered list.
    return merge(left, right)

def merge(left, right):
    """
    Merge two already sorted lists into one sorted list.
    This is a helper function used by Merge Sort.
    """

    # Result list stores the combined ordered players.
    result = []

    # Track the current index in both sorted halves.
    i = 0
    j = 0

    # Compare elements from both lists and add the smaller score to the result.
    while i < len(left) and j < len(right):

        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left list.
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right list.
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# 4. QUICK SORT

def quick_sort(players):
    """
    Quick Sort selects a pivot element and divides
    the players into three groups:

        1. Scores smaller than the pivot
        2. Scores equal to the pivot
        3. Scores greater than the pivot

    The smaller and greater groups are sorted recursively.

    Time Complexity:
        Best Case:    O(n log n)
        Average Case: O(n log n)
        Worst Case:   O(n^2)

    Space Complexity:
        O(n) for the lists used in this implementation
    """

    # A list with zero or one element is already sorted.
    if len(players) <= 1:
        return players

    # Select the middle element's score as the pivot.
    pivot = players[len(players) // 2][1]

    # Lists used to divide players based on the pivot.
    left = []
    middle = []
    right = []

    # Compare every player's score with the pivot.
    for player in players:

        if player[1] < pivot:
            left.append(player)
        elif player[1] == pivot:
            middle.append(player)
        else:
            right.append(player)

    # Sort the left and right sections recursively, then combine everything.
    return quick_sort(left) + middle + quick_sort(right)
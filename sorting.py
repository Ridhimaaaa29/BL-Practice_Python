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

    comparisons = 0
    swaps = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if players[j][1] < players[min_index][1]:
                min_index = j

        if min_index != i:
            players[i], players[min_index] = (
                players[min_index],
                players[i]
            )
            swaps += 1

    return players, comparisons, swaps

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

    comparisons = 0
    swaps = 0

    for i in range(n):
        # Used to detect whether any swapping occurred.
        swapped = False

        # Compare adjacent elements. The last i elements are already sorted.
        for j in range(n - i - 1):
            comparisons += 1

            if players[j][1] > players[j + 1][1]:
                # Swap the two players.
                players[j], players[j + 1] = (
                    players[j + 1],
                    players[j]
                )

                swaps += 1
                swapped = True

        # If no swaps occurred, the list is already sorted.
        if not swapped:
            break

    return players, comparisons, swaps

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
        return players.copy(), 0, 0

    # Find the middle position to split the list into two halves.
    mid = len(players) // 2

    # Divide the list into left and right sections.
    left = players[:mid]
    right = players[mid:]

    # Sort both halves recursively before merging them.
    left, left_comparisons, left_swaps = merge_sort(left)
    right, right_comparisons, right_swaps = merge_sort(right)

    # Merge the two sorted halves back into one ordered list.
    merged, merge_comparisons = merge(left, right)

    comparisons = (left_comparisons + right_comparisons + merge_comparisons)
    swaps = left_swaps + right_swaps

    return merged, comparisons, swaps

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

    comparisons = 0

    # Compare elements from both lists and add the smaller score to the result.
    while i < len(left) and j < len(right):
        comparisons += 1

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

    return result, comparisons

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
        return players.copy(), 0, 0

    # Select the middle element's score as the pivot.
    pivot = players[len(players) // 2][1]

    # Lists used to divide players based on the pivot.
    left = []
    middle = []
    right = []

    comparisons = 0

    # Compare every player's score with the pivot.
    for player in players:
        comparisons += 1

        if player[1] < pivot:
            left.append(player)

        elif player[1] == pivot:
            middle.append(player)

        else:
            right.append(player)

    # Sort the left and right sections recursively, then combine everything.
    left, left_comparisons, left_swaps = quick_sort(left)
    right, right_comparisons, right_swaps = quick_sort(right)

    comparisons += left_comparisons + right_comparisons
    swaps = left_swaps + right_swaps

    return left + middle + right, comparisons, swaps
from sorting import (selection_sort, bubble_sort, merge_sort, quick_sort)
from searching import binary_search
from graph import bidirectional_bfs, dfs
from monster import calculate_battle_score, find_monster
from scoring import calculate_final_score, determine_rank


def main():

    print("\n===== ALGORITHM ARENA =====")
    # mission 1: building the leaderboard using sorting algorithms.
    print("\n===== LEADERBOARD =====")

    players = [
        ("Arjun", 450),
        ("Riya", 720),
        ("Kabir", 310),
        ("Neha", 890),
        ("Aman", 560)
    ]

    print("\nChoose Sorting Algorithm:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Merge Sort")
    print("4. Quick Sort")

    try:
        choice = int(input("\nEnter choice: "))
    except ValueError:
        print("Invalid sorting choice.")
        return

    if choice == 1:
        sorted_players, sorting_comparisons, sorting_swaps = selection_sort(players)
        algorithm_name = "Selection Sort"

    elif choice == 2:
        sorted_players, sorting_comparisons, sorting_swaps = bubble_sort(players)
        algorithm_name = "Bubble Sort"

    elif choice == 3:
        sorted_players, sorting_comparisons, sorting_swaps = merge_sort(players)
        algorithm_name = "Merge Sort"

    elif choice == 4:
        sorted_players, sorting_comparisons, sorting_swaps = quick_sort(players)
        algorithm_name = "Quick Sort"

    else:
        print("Invalid sorting choice.")
        return

    print(f"\nLeaderboard using {algorithm_name}:\n")

    for player in sorted_players:
        print(player[0], player[1])

    # The leaderboard is sorted in ascending order. Therefore, the last player has the highest score.
    leaderboard_score = sorted_players[-1][1]


    # mission 2: treasure scanner
    print("\n===== TREASURE SCANNER =====")
    treasures = [105, 118, 129, 145, 167, 189, 205, 221, 250]

    try:
        target = int(input("\nEnter Treasure ID: "))

    except ValueError:
        print("Invalid Treasure ID.")
        return

    treasure_index, binary_search_comparisons = binary_search(
        treasures,
        target
    )

    if treasure_index != -1:

        treasure_bonus = 100
        print("\nTreasure Found!")
        print("Index:", treasure_index)
    else:

        print("\nTreasure Not Found!")
        treasure_bonus = 0

    # mission 3: fastest route 
    print("\n===== FASTEST ROUTE =====")

    kingdom_graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C", "G"],
        "G": ["E", "F"]
    }

    start = input("\nEnter Start City: ").strip().upper()
    destination = input("Enter Destination City: ").strip().upper()

    shortest_path, steps, bfs_nodes_visited = bidirectional_bfs(
        kingdom_graph,
        start,
        destination
    )

    if shortest_path:
        print("\nShortest Route:")
        print(" -> ".join(shortest_path))
        print("Steps:", steps)
    else:
        print("\nNo route found!")

    # mission 4: kingdom exploration
    print("\n===== KINGDOM EXPLORATION =====")

    exploration_start = input("\nEnter Starting Location: ").strip().upper()

    if exploration_start not in kingdom_graph:
        print("\nInvalid starting location.")
        exploration_order = []
        dfs_nodes_visited = 0
        exploration_bonus = 0

    else:
        exploration_order, dfs_nodes_visited = dfs(
            kingdom_graph,
            exploration_start
        )

        print("\nDFS Exploration Order:")
        print(" -> ".join(exploration_order))

        if len(exploration_order) == len(kingdom_graph):
            exploration_bonus = 100
        else:
            exploration_bonus = 0

    # mission 5: monster battle
    print("\n===== MONSTER BATTLE =====")

    monsters = [
        {
            "name": "Goblin",
            "health": 100,
            "attack": 20,
            "reward": 50
        },
        {
            "name": "Dragon",
            "health": 500,
            "attack": 80,
            "reward": 500
        },
        {
            "name": "Orc",
            "health": 250,
            "attack": 40,
            "reward": 150
        },
        {
            "name": "Troll",
            "health": 350,
            "attack": 60,
            "reward": 300
        }
    ]

    monster_name = input("\nChoose a monster: ").strip()
    monster = find_monster(monsters, monster_name)

    if monster is None:
        print("Monster not found!")
        battle_score = 0
    else:
        battle_score = calculate_battle_score(
            monster["health"],
            monster["attack"],
            monster["reward"]
        )

        # The game uses whole-number scores.
        battle_score = int(battle_score)
        print(f"\nMonster: {monster['name']}")
        print("Battle Score:", battle_score)

    # final game score and rank calculation

    final_score = calculate_final_score(
        leaderboard_score,
        treasure_bonus,
        battle_score,
        exploration_bonus
    )

    rank = determine_rank(final_score)

    print("\n===== GAME RESULT =====")

    print("Player Score:", leaderboard_score)
    print("Treasure Bonus:", treasure_bonus)
    print("Battle Score:", battle_score)
    print("Exploration Bonus:", exploration_bonus)
    print("Final Score:", final_score)
    print("Rank:", rank)


    # bonus challenge: game performance dashboard
    print("\n===== ALGORITHM PERFORMANCE =====")

    # Run all four sorting algorithms to compare their performance.
    selection_result, selection_comparisons, selection_swaps = selection_sort(players)
    bubble_result, bubble_comparisons, bubble_swaps = bubble_sort(players)
    merge_result, merge_comparisons, merge_swaps = merge_sort(players)
    quick_result, quick_comparisons, quick_swaps = quick_sort(players)

    print("\nSelection Sort")
    print("Comparisons:", selection_comparisons)
    print("Swaps:", selection_swaps)

    print("\nBubble Sort")
    print("Comparisons:", bubble_comparisons)
    print("Swaps:", bubble_swaps)

    print("\nMerge Sort")
    print("Comparisons:", merge_comparisons)
    print("Swaps:", merge_swaps)

    print("\nQuick Sort")
    print("Comparisons:", quick_comparisons)
    print("Swaps:", quick_swaps)

    print("\nBinary Search")
    print("Comparisons:", binary_search_comparisons)

    print("\nBidirectional BFS")
    print("Nodes Visited:", bfs_nodes_visited)

    print("\nDFS")
    print("Nodes Visited:", dfs_nodes_visited)

    # Determine which sorting algorithm performed best
    # based on the number of comparisons.
    sorting_performance = {
        "Selection Sort": selection_comparisons,
        "Bubble Sort": bubble_comparisons,
        "Merge Sort": merge_comparisons,
        "Quick Sort": quick_comparisons
    }

    best_sorting_algorithm = min(
        sorting_performance,
        key=sorting_performance.get
    )

    print("\nWhich sorting algorithm performed best?")
    print(best_sorting_algorithm)

    print("\nWhich algorithm found the treasure?")
    print("Binary Search")

    print("\nWhich algorithm found the shortest route?")
    print("Bidirectional BFS")

    print("\nWhich algorithm explored the entire kingdom?")

    if dfs_nodes_visited == len(kingdom_graph):
        print("DFS")
    else:
        print("DFS explored", dfs_nodes_visited, "nodes.")


if __name__ == "__main__":
    main()
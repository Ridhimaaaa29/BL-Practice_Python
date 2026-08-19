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
        sorted_players = selection_sort(players)
        algorithm_name = "Selection Sort"

    elif choice == 2:
        sorted_players = bubble_sort(players)
        algorithm_name = "Bubble Sort"

    elif choice == 3:
        sorted_players = merge_sort(players)
        algorithm_name = "Merge Sort"

    elif choice == 4:
        sorted_players = quick_sort(players)
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

    treasure_index = binary_search(treasures, target)

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
    shortest_path, steps = bidirectional_bfs(kingdom_graph, start, destination) 

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
        exploration_bonus = 0
    else:
        exploration_order = dfs(kingdom_graph, exploration_start)
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


if __name__ == "__main__":
    main()
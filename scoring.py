# functions for calculating the final game score and determining the player's final rank.
def calculate_final_score(leaderboard_score, treasure_bonus, battle_score, exploration_bonus):
    return (
        leaderboard_score
        + treasure_bonus
        + battle_score
        + exploration_bonus
    )

def determine_rank(score):
    if score <= 299:
        return "NOVICE EXPLORER"
    elif score <= 599:
        return "SKILLED ADVENTURER"
    elif score <= 999:
        return "MASTER STRATEGIST"
    else:
        return "ALGORITHM LEGEND"

def get_rank(score):
    return determine_rank(score)
def calculate_battle_score(health, attack, reward):
    return reward + (health / 10) - attack

def find_monster(monsters, name):
    for monster in monsters:
        if monster["name"].lower() == name.lower():
            return monster
    return None
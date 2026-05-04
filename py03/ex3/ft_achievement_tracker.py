#!/usr/bin/env python3
import random

achievement_list = (
    "First Level Cleared",
    "Master of Stealth",
    "Treasure Hunter",
    "Invincible",
    "Perfect Combo",
    "World Explorer",
    "Multiplayer King",
    "Legendary Collector",
    "Extreme Speed",
    "Secret Ending Unlocked",
    "Boss Slayer",
    "Puzzle Master",
    "Untouchable",
    "Hidden Secrets Found",
    "Ultimate Survivor",
    "Combo Breaker",
    "Speedrun Champion",
    "Elite Sniper",
    "Dungeon Conqueror",
    "Completionist")


def assign_achievements(achivement) -> set:
    achieve_number = random.randrange(3, int(len(achivement) * 0.5))
    return set(random.sample(achivement, achieve_number))


class Player():
    def __init__(self, name: str, achievements: set):
        self.name = name
        self.achievements = achievements


def ft_achievement_tracker():

    players = [
        Player(f"player_{i}", assign_achievements(achievement_list))
        for i in range(1, 5)
    ]
    print("=== Starting... ===\n")
    for player in players:
        print(f"{player.name.capitalize()
                 }, achievements: {player.achievements}")

    all_achievements = set().union(*
                                   (player.achievements for player in players))
    print(f"\nAll distinct achievements:\n===\n\n{all_achievements}\n\n===")
    common_achievements = set.intersection(
        *(player.achievements for player in players))
    print(f"\nCommon Achievements: {common_achievements}")
    print("\n===")
    for player in players:
        other_players = [p for p in players if p is not player]
        unique = player.achievements.difference(
            *(other.achievements for other in other_players)
        )
        print(f"\n{player.name.capitalize()} has unique: {unique}")

    print("\n===")
    for player in players:
        missing = all_achievements.difference(player.achievements)
        print(f"\n{player.name.capitalize()} is missing: {missing}")
    print("\n===")


if __name__ == "__main__":
    ft_achievement_tracker()

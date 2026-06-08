import random
from typing import Tuple, Sequence, Set, List

achievement_list: Tuple[str, ...] = (
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
    "Completionist",
)


def assign_achievements(achievement: Sequence[str]) -> Set[str]:
    # ensure an upper bound that's at least 3 so randint works for small lists
    max_count = max(3, int(len(achievement) * 0.5))
    achieve_number = random.randint(3, max_count)
    return set(random.sample(achievement, achieve_number))


class Player:
    def __init__(self, name: str, achievements: Set[str]) -> None:
        self.name: str = name
        self.achievements: Set[str] = achievements


def ft_achievement_tracker() -> None:
    players: List[Player] = [
        Player(f"player_{i}", assign_achievements(achievement_list))
        for i in range(1, 5)
    ]
    print("=== Starting... ===\n")
    for player in players:
        print(f"{player.name.capitalize()}, "
              f"achievements: {player.achievements}")

    all_achievements: Set[str] = set().union(
        *(player.achievements for player in players)
    )
    print(f"\nAll distinct achievements:\n===\n\n{all_achievements}\n\n===")

    if players:
        archievements = players[0].achievements
        common_achievements: Set[str] = set(archievements).intersection(
            *(p.achievements for p in players[1:])
        )
    else:
        common_achievements = set()
    print(f"\nCommon Achievements: {common_achievements}")
    print("\n===")

    for player in players:
        other_players: List[Player] = [p for p in players if p is not player]
        unique: Set[str] = player.achievements.difference(
            *(other.achievements for other in other_players)
        )
        print(f"\n{player.name.capitalize()} has unique: {unique}")

    print("\n===")
    for player in players:
        missing: Set[str] = all_achievements.difference(player.achievements)
        print(f"\n{player.name.capitalize()} is missing: {missing}")
    print("\n===")


if __name__ == "__main__":
    ft_achievement_tracker()

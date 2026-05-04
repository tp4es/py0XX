#!/usr/bin/env python3

from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "Scorpion",
        "Sub-Zero",
        "Sonya",
        "Kitana",
        "Yori Yagami",
        "Kio Kusanagi",
        "Blue Mary",
        "Shermie",
        "Nina Williams"]
    actions = ["jab", "kick", "uppercut", "throw", "SUPER", "block"]

    while True:
        player, rival = random.sample(players, 2)
        action = random.choice(actions)
        rival_action = random.choice(actions)

        roll_player = random.randint(
            1, 6) if action != "SUPER" else random.randint(
            3, 12)
        roll_rival = random.randint(
            1, 6) if rival_action != "SUPER" else random.randint(
            3, 12)
        if roll_player > roll_rival:
            result = "wins"
        elif roll_player < roll_rival:
            result = "loses"
        else:
            result = "draws"

        description = (
            f"vs {rival}: {action} ({roll_player}) vs "
            f"{rival_action} ({roll_rival}) -> {result}"
        )
        yield (player, description)


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while events:
        idx = random.randrange(len(events))
        yield events.pop(idx)


def main() -> None:
    stream = gen_event()

    for _ in range(1000):
        print(next(stream))

    ten_events = [next(stream) for _ in range(10)]
    for event in consume_event(ten_events):
        print(f"Deleted: {event}")
        print(f"Remaining: {ten_events}")


if __name__ == "__main__":
    main()

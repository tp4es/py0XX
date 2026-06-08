#!/usr/bin/env python3
import random

players: list[str] = [
    "scorpion",
    "sub-Zero",
    "sonya",
    "Kitana",
    "Yori Yagami",
    "Kio Kusanagi",
    "Blue Mary",
    "shermie",
    "Nina Williams"]


def ft_data_alchemist() -> None:
    print(f"Original Names: {players}")
    new_capi = [p.title() for p in players]
    old_capi = [p for p in players if p.title() == p]
    print(f"Capitalized: {new_capi}.\nOnly capis: {old_capi}")
    new_dict = {name: random.randint(100, 9999) for name in new_capi}
    avg = round(sum(new_dict.values()) / len(new_dict))
    print(f"My dictionarie: {new_dict}.\n Average Score: {avg}")
    hs_dict = {n: s for n, s in new_dict.items() if s > avg}
    print(hs_dict)


if __name__ == "__main__":
    ft_data_alchemist()

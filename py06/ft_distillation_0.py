#!/usr/bin/env	python3

from alchemy.potions import healing_potion, strength_potion


def create_potions() -> None:
    print("=== Potions Service===\n")
    try:
        print(f"Trying healing potion:\n{healing_potion()}")
        print(f"Trying strength potion:\n{strength_potion()}")
    except AttributeError as e:
        print(f"Error found: {e}")


if __name__ == "__main__":
    create_potions()

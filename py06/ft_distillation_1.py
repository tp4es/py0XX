#!/usr/bin/env	python3

import alchemy


def create_potions() -> None:
    print("=== Potions Service===\n")
    try:
        print(f"Trying healing potion:\n{alchemy.special_heal()}")
        print(f"Trying strength potion:\n{alchemy.original_strength()}")
    except Exception as e:
        print(f"Error found: {e}")


if __name__ == "__main__":
    create_potions()

#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory
import random


creatures_list = []


def flame_factory() -> None:
    print("=== TESTING FIRE ===")
    try:
        charmander = FlameFactory.create_base(None, name="charmander")
        if charmander:
            print(charmander.describe())
            print(f"{charmander.attack()}")
            creatures_list.append(charmander)
        charizard = FlameFactory.create_evolved(None, name="Charizard")
        if charizard:
            print(charizard.describe())
            print(charizard.attack())
            creatures_list.append(charizard)
    except Exception as e:
        print(f"Caught Error: {e}")


def aqua_factory() -> None:
    print("=== TESTING AQUA ===")
    try:
        squartle = AquaFactory.create_base(None, name="squartle")
        if squartle:
            print(squartle.describe())
            print(f"{squartle.attack()}")
            creatures_list.append(squartle)
        blastoise = AquaFactory.create_evolved(None, name="blastoise")
        if blastoise:
            print(blastoise.describe())
            print(blastoise.attack())
            creatures_list.append(blastoise)
    except Exception as e:
        print(f"Caught Error: {e}")


def ft_battle():
    print("=== TESTING Battle ===")
    try:
        creature1, creature2 = random.sample(creatures_list, 2)
        print(creature1.describe())
        print("VS.")
        print(creature2.describe())
        print(creature1.attack())
        print(creature2.attack())
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    flame_factory()
    aqua_factory()
    ft_battle()

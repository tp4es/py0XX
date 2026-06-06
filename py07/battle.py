#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory
from typing import cast


def ft_factory(factory: CreatureFactory) -> None:
    print("=== TESTING FACTORY ===")
    try:
        base_creature = factory.create_base()
        if base_creature:
            print(base_creature.describe())
            print(f"{base_creature.attack()}")
        evolved_creature = factory.create_evolved()
        if evolved_creature:
            print(evolved_creature.describe())
            print(evolved_creature.attack())
    except Exception as e:
        print(f"Caught Error: {e}")


def ft_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("=== TESTING Battle ===")
    try:
        creature1 = factory1.create_base()
        creature2 = factory2.create_base()
        print(creature1.describe())
        print("VS.")
        print(creature2.describe())
        print(creature1.attack())
        print(creature2.attack())
    except Exception as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    ft_factory(FlameFactory())
    ft_factory(AquaFactory())
    ft_battle(FlameFactory(), AquaFactory())

#!/usr/bin/env	python3
from alchemy import create_air
from alchemy import create_earth
from ..elements import create_water, create_fire

elements = []


def healing_potion() -> str:
    try:
        elements.append(create_air(), create_earth())
    except AttributeError as e:
        print(f"Error Found: {e}")
    return (
        f"Healing potion brewed with '{elements[0]}' and"
        f" '{elements[1]}'"
    )


def strength_potion() -> str:
    try:
        elements.append(create_fire())
        elements.append(create_water())
    except AttributeError as e:
        print(f"Error found: {e}")
    return (
        f"Strength potion brewed with '{elements[2]}' and"
        f" '{elements[3]}'"
    )

#!/usr/bin/env python3

class Plants:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    """Get/Setter methods"""
    @property
    def proper_height(self) -> int:
        return self._height

    @proper_height.setter
    def proper_height(self, value: int) -> None:
        if value > 0:
            self._height = value
        else:
            print("Height cannot be negative.")

    @property
    def proper_age(self) -> int:
        return self._age

    @proper_age.setter
    def proper_age(self, value: int) -> None:
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative.")


def ft_garden_security() -> None:
    plant1 = Plants("rose", 25, 30)
    plant2 = Plants("sunflower", 80, 45)
    plant3 = Plants("cactus", 15, 120)

    plants_list = [plant1, plant2, plant3]
    print("=== Garden Plant Security ===\n")
    for plant_name in plants_list:
        print(
            f"{plant_name.name.capitalize()}: "
            f"{plant_name.proper_height}cm, {plant_name.proper_age} days old.")
    print("\n=== Plants Updates ===\n")
    plant1.proper_age = 1
    plant2.proper_height = 125
    print(
        f"Updated: \n{plant1.name.capitalize()}, "
        f"new value (age) = {plant1.proper_age}.")
    print(f"{plant2.name.capitalize()}, new value (height) = "
          f"{plant2.proper_height}.")
    print("\n=== Plants Invalid Updates ===\n")
    plant3.proper_age = -1
    print(f"{plant3.name.capitalize()}, tried age = -1, current value = "
          f"{plant3.proper_age}.")
    plant3.proper_height = -100
    print(f"{plant3.name.capitalize()}, tried height = -100, "
          f"current value = {plant3.proper_height}.\n")


if __name__ == "__main__":
    ft_garden_security()

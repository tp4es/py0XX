#!/usr/bin/env python3

class Plants:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, days: int):
        grow_fact = ((20 / (self.age + days)) + (25 / self.height))
        const = (self.height / self.age) * grow_fact
        self.height += int(const)
        self.age += 1

    def aged(self, days):
        self.grow(days)
        print(
            f"{self.name.capitalize()}: {int(self.height)}cm, {
                int(self.age)} days old.\n")


def ft_plant_growth():
    plant1 = Plants("rose", 25, 30)
    plant2 = Plants("sunflower", 80, 45)
    plant3 = Plants("cactus", 15, 120)
    plants_list = [plant1, plant2, plant3]
    print("=== Garden Plant Growth ===\n")
    for plant_name in plants_list:
        print(f"{plant_name.name.capitalize()}: {plant_name.height}cm, {
            plant_name.age} days old.")
    for i in range(1, 8):
        print(f"\n=== Day {i}===\n")
        for plant_name in plants_list:
            plant_name.aged(i)


if __name__ == "__main__":
    ft_plant_growth()

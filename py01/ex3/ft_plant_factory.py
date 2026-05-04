#!/usr/bin/env python3

class Plants:
    def __init__(self, name: str = "default", height: int = 0, age: int = 0):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name.capitalize()}: {
                int(self.height)}cm, {int(self.age)} days old.\n")


def ft_plant_factory():
    plant1 = Plants("rose", 25, 30)
    plant2 = Plants("sunflower", 80, 45)
    plant3 = Plants("cactus", 15, 120)
    plant4 = Plants("tulip", 10, 20)
    plant5 = Plants("daisy", 5, 10)
    plant0 = Plants()
    plants_list = [plant1, plant2, plant3, plant4, plant5, plant0]
    print("=== Plant Factory Output ===\n")
    for plant_name in plants_list:
        plant_name.show()


if __name__ == "__main__":
    ft_plant_factory()

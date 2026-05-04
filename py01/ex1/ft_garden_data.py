#!/usr/bin/env python3

class Plants():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name.capitalize()}: {
                str(self.height)}cm, {str(self.age)} days old.")


def ft_garden_data():
    plant1 = Plants("rose", 25, 30)
    plant2 = Plants("sunflower", 80, 45)
    plant3 = Plants("cactus", 15, 120)
    plants_list = [plant1, plant2, plant3]
    for plant_name in plants_list:
        plant_name.show()


if __name__ == "__main__":
    ft_garden_data()

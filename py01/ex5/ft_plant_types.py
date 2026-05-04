#!/usr/bin/env python3

class Plants:

    def __init__(self, name: str, heigh: int, age: int):
        self.name = name
        self._height = heigh
        self._age = age

    @property
    def proper_height(self):
        return self._height

    @proper_height.setter
    def proper_height(self, value: int):
        if value > 0:
            self._height = value
        else:
            print("Height cannot be negative.\n")

    @property
    def proper_age(self):
        return self._age

    @proper_age.setter
    def proper_age(self, value: int):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative.\n")

    """Father method to be overridden by subclasses"""

    def show(self):
        print(f"{self.name.capitalize()}, {
            self._height:.2f}cm, {self._age} days old.")

    def grow(self, days: int):
        grow_fact = (self._height / self._age)
        const = grow_fact * (1 + (30 / (self._age + days)))
        self._height += int(const)
        self._age += days

    def aged(self, days):
        self.grow(days)


class Flower(Plants):
    def __init__(self, name: str, heigh: int, age: int, color: str):
        super().__init__(name, heigh, age)
        self.color = color

    def bloom(self):
        print(f"{self.name.capitalize()
                 } is blooming with {self.color} color!\n")

    def show(self):
        super().show()
        print(f"Color: {self.color}")


class Tree(Plants):
    def __init__(self, name: str, heigh: int, age: int, trunk_diameter: float):
        super().__init__(name, heigh, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = (self._height * 0.5) + (self.trunk_diameter * 0.3)
        print(
            f"{self.name.capitalize()} produces {
                shade:.2f} square centimeters of shade.\n")

    def show(self):
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter:.2f}cm")

    def grow(self, days: int):
        super().grow(days)
        self.trunk_diameter += (days * 0.1) * (self._height / self._age)


class Vegetable(Plants):
    def __init__(
            self,
            name: str,
            heigh: int,
            age: int,
            harvest_season: str,
            nutritional_value: float = 0):
        super().__init__(name, heigh, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(
            f"Harvest Season: {
                self.harvest_season}, Nutritional Value: {
                self.nutritional_value:.2f}.\n")

    def grow(self, days: int):
        super().grow(days)
        self.nutritional_value += (1 * days) * (40 / (self._age + days))


def ft_plant_types():
    flower1 = Flower("rose", 25, 30, "red")
    tree1 = Tree("oak", 800, 4594, 80)
    vegetable1 = Vegetable("carrot", 15, 95, "autumn")

    print("=== Plant Types ===\n")
    my_list = [flower1, tree1, vegetable1]
    for plant in my_list:
        plant.show()
    print("\n=== Special Abilities ===\n")
    flower1.bloom()
    tree1.produce_shade()
    print("=== Growth Simulation ===\n")
    i: int = 500
    print(f"Making the plants grow for {i} days...\n")
    for plant in my_list:
        plant.aged(i)
        plant.show()


if __name__ == "__main__":
    ft_plant_types()

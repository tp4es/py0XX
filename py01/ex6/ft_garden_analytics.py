#!/usr/bin/env python3

class Plants:

    count_show: int = 0
    count_grow: int = 0
    count_aged: int = 0
    count_special: int = 0

    def __init__(
            self,
            name: str = "Unknown plant",
            heigh: int = 0,
            age: int = 0):
        self.name = name
        self._height = heigh
        self._age = age

    @classmethod
    def creat(cls):
        name = "unknown plant"
        age = 0
        height = 0
        return cls(name, height, age)

    def statistics(self):
        print(f"\tTotal show calls: {self.count_show}")
        print(f"\tTotal grow calls: {self.count_grow}")
        print(f"\tTotal aged calls: {self.count_aged}")
        print(f"\tTotal special calls: {self.count_special}")

        """ === Getters and Setters for height and age with validation === """
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
        self.count_show += 1
        print(f"{self.name.capitalize()}, {
            self._height:.2f}cm, {self._age} days old.")

    def grow(self, days: int):
        self.count_grow += 1
        grow_fact = (self._height / self._age) if self._age > 0 else 0
        const = grow_fact * (1 + (30 / (self._age + days)))
        self._height += int(const)
        self._age += days

    def aged(self, days):
        self.count_aged += 1
        self.grow(days)

    @staticmethod
    def days2years(age: int):
        if age >= 365:
            years = age / 365
            days = age % 365
            return f"Total: {int(years)} years and {days} days"
        else:
            return f"Total: {age} days < 1 year"

    """ === Flower sub-class === """


class Flowers(Plants):
    def __init__(
            self,
            name: str,
            heigh: int,
            age: int,
            color: str,
            blooming: bool = False):
        super().__init__(name, heigh, age)
        self.color = color
        self.blooming = blooming

    def bloom(self):
        self.count_special += 1
        if not self.blooming:
            self.blooming = True
            print(f"{self.name.capitalize()
                     } is blooming with {self.color} color!.")

    def show(self):
        super().show()
        print(
            f"Color: {
                self.color}, Blooming: {
                'Yes' if self.blooming else 'No'}.")

        """ === childish class"""


class Seed(Flowers):
    def __init__(
            self,
            name: str,
            heigh: int,
            age: int,
            color: str,
            qty: int = 0):
        super().__init__(name, heigh, age, color, blooming=False)
        self.name = self.name + " seed"
        self.qty = qty

    def show(self):
        super().show()
        print(f"Seeds: {self.qty if self.blooming else '0'}.")

    def grow(self, days: int):
        super().grow(days)
        self.qty += int((1 * days) * (10 / (self._age + days)))

    """ === Tree sub-class === """


class Trees(Plants):
    def __init__(self, name: str, heigh: int, age: int, trunk_diameter: float):
        super().__init__(name, heigh, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        self.count_special += 1
        shade = (self._height * 0.5) + (self.trunk_diameter * 0.3)
        print(
            f"{self.name.capitalize()
               } produces {shade:.2f} square centimeters of shade.\n")

    def show(self):
        super().show()
        print(f"Trunk Diameter: {self.trunk_diameter:.2f}cm")

    def grow(self, days: int):
        super().grow(days)
        self.trunk_diameter += (days * 0.1) * (self._height / self._age)

    """ === Vegetable sub-class === """


class Vegetables(Plants):
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


def garden_analytics():
    i: int = 150
    sunflower = Flowers("sunflower", 30, 10, "yellow")
    seed = Seed("sunflower", 1, 1, "yellow", qty=100)
    oak = Trees("oak", 200, 100, 50)
    tomato = Vegetables("tomato", 50, 20, "summer")
    plant = Plants.creat()
    list_plants = [sunflower, seed, oak, tomato]
    print("=== Initial State ===\n")
    for p in list_plants:
        p.show()
    plant.show()
    print(f"\n=== After Growing for {i} days ===\n")
    for p in list_plants:
        p.aged(i)
        p.show()
    print("\n=== Special Actions ===\n")
    sunflower.bloom()
    oak.produce_shade()
    print("\n=== Final Statistics ===\n")
    for p in list_plants:
        print(f"{p.name.capitalize()} statistics:")
        p.statistics()
    print(f"{plant.name.capitalize()} statistics:")
    plant.statistics()


if __name__ == "__main__":
    garden_analytics()

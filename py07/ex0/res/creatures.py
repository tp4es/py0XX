from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def describe(self) -> str:
        return f"{self.name} is a {self.type}"

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Fire")

    def attack(self) -> str:
        return f"{self.name} attacks with fire!"


class Pyrodon(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} attacks with a fiery roar!"


class Aquabub(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water")

    def attack(self) -> str:
        return f"{self.name} attacks with a water blast!"


class Torragon(Creature):
    def __init__(self, name: str):
        super().__init__(name, "Water/Dragon")

    def attack(self) -> str:
        return f"{self.name} attacks with a dragon roar!"

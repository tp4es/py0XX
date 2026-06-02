from ex0 import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name, "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Creature) -> str:
        if isinstance(target, Sproutling):
            target.health += 20
            return f"{self.name} heals {target.name} for 20 health!"
        return f"{self.name} cannot heal {target.name}."


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str):
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Storm!"

    def heal(self, target: Creature) -> str:
        if isinstance(target, HealCapability):
            return f"{self.name} heals {target.name} for 30 health!"
        return f"{self.name} cannot heal {target.name}."


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str):
        super().__init__(name, "Normal")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} uses Hyper Beam!"
        return f"{self.name} uses Tackle!"

    def transform(self) -> str:
        self._transformed = True
        return (
           f"{self.name} transforms into a powerful form!"
           f"{self.attack()}")

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} reverts to its original form!"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str):
        super().__init__(name, "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} uses draconic attack!"
        return f"{self.name} uses hit!"

    def transform(self) -> str:
        self._transformed = True
        return (
           f"{self.name} transforms into a draconic battle form!"
           f"{self.attack()}")

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} reverts to its original form!"

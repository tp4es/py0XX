from ex1.families import Sproutling, Bloomelle, Shiftling, Morphagon
from ex0.factorizer import CreatureFactory


class HealingCreatureFactory(CreatureFactory):
    def create_base(self, name: str = "Sproutling") -> Sproutling:
        return Sproutling(name)

    def create_evolved(self, name: str = "Bloomelle") -> Bloomelle:
        return Bloomelle(name)


class TransformCreatureFactory(CreatureFactory):
    def create_base(self, name: str = "Shiftling") -> Shiftling:
        return Shiftling(name)

    def create_evolved(self, name: str = "Morphagon") -> Morphagon:
        return Morphagon(name)

from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str = "base") -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, name: str = "evolved") -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, name: str = "Flameling") -> Creature:
        return Flameling(name)

    def create_evolved(self, name: str = "Pyrodon") -> Creature:
        return Pyrodon(name)


class AquaFactory(CreatureFactory):
    def create_base(self, name: str = "Aquabub") -> Creature:
        return Aquabub(name)

    def create_evolved(self, name: str = "Torragon") -> Creature:
        return Torragon(name)

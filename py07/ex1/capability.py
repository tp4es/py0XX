from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

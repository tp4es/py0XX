from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capability import HealCapability, TransformCapability
import ex2.error_sys


class BattleStrategy(ABC):
    @abstractmethod
    def act() -> None:
        pass

    @abstractmethod
    def is_valid() -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self) -> None:
        if self.is_valid():
            self.attack()

    def is_valid(self) -> bool:
        try:
            if isinstance(self, Creature):
                return True
        except Exception as e:
            raise ex2.error_sys.CreatureStrategyError(self) from e


class AggresiveStrategy(BattleStrategy):
    def act(self) -> None:
        if self.is_valid():
            self.transform()
            self.attack()
            self.revert()

    def is_valid(self) -> bool:
        try:
            if isinstance(self, TransformCapability()):
                return True
        except Exception as e:
            raise ex2.error_sys.AgressiveStrategyError(self) from e


class DefensiveStrategy(BattleStrategy):
    def act(self) -> None:
        if self.is_valid():
            self.attack()
            self.heal()

    def is_valid(self) -> bool:
        try:
            if isinstance(self, HealCapability()):
                return True
        except Exception as e:
            raise ex2.error_sys.DefensiveStrategyError(self) from e

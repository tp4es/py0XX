from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capability import HealCapability, TransformCapability
import ex2.error_sys


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature | TransformCapability | HealCapability
            ) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        try:
            if self.is_valid(creature):
                print(creature.attack())
        except Exception as e:
            raise ex2.error_sys.CreatureStrategyError(creature) from e

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggresiveStrategy(BattleStrategy):
    def act(self, creature: TransformCapability) -> None:
        try:
            if self.is_valid(creature):
                print(
                    f"{creature.transform()}\n",
                    f"{creature.attack()}\n",
                    f"{creature.revert()}"
                )
        except Exception as e:
            raise ex2.error_sys.AgressiveStrategyError(creature) from e

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        try:
            if self.is_valid(creature):
                print(
                    f"{creature.attack()}\n",
                    f"{creature.heal(creature)}"
                )
        except Exception as e:
            raise ex2.error_sys.DefensiveStrategyError(creature) from e

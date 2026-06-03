from ex0.factorizer import AquaFactory, FlameFactory
from ex0.creatures import Creature
from ex1.factorizer import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability
from ex2.rules import BattleStrategy, NormalStrategy, AggresiveStrategy, DefensiveStrategy


cards = []
factories = [
    AquaFactory, FlameFactory, HealingCreatureFactory, TransformCreatureFactory]


def strategy_match(creature: Creature) -> BattleStrategy:
    if isinstance(creature, HealCapability):
        return DefensiveStrategy()
    elif isinstance(creature, TransformCapability):
        return AggresiveStrategy()
    else:
        return NormalStrategy()


def create() -> tuple:
    try:
        for factory in factories:
            base = factory.create_base(None)
            strategy_base = strategy_match(base)
            evolved = factory.create_evolved(None)
            strategy_evolved = strategy_match(evolved)
            try:
                cards.append((base, strategy_base))
                cards.append((evolved, strategy_evolved))
            except Exception as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def tournament() -> None:
    create()
    for i in range(len(cards)):
        for j in range(i + 1, len(cards) - 1):
            try:
                print(f"\n=== !FIGHT! ===")
                print(cards[i][0].describe())
                print("VS.")
                print(cards[j][0].describe())
                print(cards[i][1].act())
                print(cards[j][1].act())
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    tournament()

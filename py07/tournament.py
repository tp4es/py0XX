from ex0.factorizer import AquaFactory, FlameFactory
from ex0.creatures import Creature
from ex1.factorizer import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability
from ex2.rules import NormalStrategy, AggresiveStrategy, DefensiveStrategy
from ex2.rules import BattleStrategy

cards: list[tuple[Creature, BattleStrategy]] = []
factories = [
    AquaFactory(), FlameFactory(),
    HealingCreatureFactory(), TransformCreatureFactory()
]


def strategy_match(creature: Creature) -> BattleStrategy:
    if isinstance(creature, HealCapability):
        return DefensiveStrategy()
    elif isinstance(creature, TransformCapability):
        return AggresiveStrategy()
    else:
        return NormalStrategy()


def create() -> None:
    try:
        for factory in factories:
            base = factory.create_base()
            strategy_base = strategy_match(base)
            evolved = factory.create_evolved()
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
        for j in range(i + 1, len(cards)):
            try:
                print("\n=== !FIGHT! ===")
                print(cards[i][0].describe())
                print("VS.")
                print(cards[j][0].describe())
                cards[i][1].act(cards[i][0])
                cards[j][1].act(cards[j][0])
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    tournament()

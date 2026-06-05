from ex1.factorizer import HealingCreatureFactory, TransformCreatureFactory
from ex0.factorizer import CreatureFactory


def ft_factory(factory: CreatureFactory) -> None:
    try:
        base_creature = factory.create_base()
        print(base_creature.describe())
        print(f"{base_creature.attack()}")
    except Exception as e:
        print(f"Caught Error: {e}")


def ft_healer():
    try:
        print("=== Testing Creature Healer ===")
        creature = HealingCreatureFactory.create_base(None)
        print(creature.describe())
        print(creature.attack())
        print(creature.heal(creature))
    except Exception as e:
        print(f"Error Caught: {e}")
    try:
        print("=== Testing Creature Evolved Healer ===")
        creature1 = HealingCreatureFactory.create_evolved(None)
        print(creature1.describe())
        print(creature1.attack())
        print(creature1.heal(creature))
    except Exception as e:
        print(f"Error Caught: {e}")


def ft_transformer():
    try:
        print("=== Testing Creature Transformer_base ===")
        transformer = TransformCreatureFactory.create_base(None)
        print(transformer.describe())
        print(transformer.attack())
        print(transformer.transform())
        print(transformer.attack())
        print(transformer.revert())
    except Exception as e:
        print(f"Error Caught: {e}")
    try:
        print("=== Testing Creature Transformer_Evolved ===")
        transformer1 = TransformCreatureFactory.create_evolved(None)
        print(transformer1.describe())
        print(transformer1.attack())
        print(transformer1.transform())
        print(transformer1.attack())
        print(transformer1.revert())
    except Exception as e:
        print(f"Error Caught: {e}")


if __name__ == "__main__":
    ft_healer()
    ft_transformer()

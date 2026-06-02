from ex1.factorizer import HealingCreatureFactory, TransformCreatureFactory


def ft_healer():
    try:
        print("=== Testing Creature Healer ===")
        creature = HealingCreatureFactory.create_base(None, "Healer")
        print(creature.describe())
        print(creature.attack())
        print(creature.heal(creature))
    except Exception as e:
        print(f"Error Caught: {e}")
    try:
        print("=== Testing Creature Evolved Healer ===")
        creature1 = HealingCreatureFactory.create_evolved(
            None, "evolved Healer")
        print(creature1.describe())
        print(creature1.attack())
        print(creature1.heal(creature))
    except Exception as e:
        print(f"Error Caught: {e}")


def ft_transformer():
    try:
        print("=== Testing Creature Transformer_base ===")
        transformer = TransformCreatureFactory.create_base(None, "Trans")
        print(transformer.describe())
        print(transformer.attack())
        print(transformer.transform())
        print(transformer.attack())
        print(transformer.revert())
    except Exception as e:
        print(f"Error Caught: {e}")
    try:
        print("=== Testing Creature Transformer_Evolved ===")
        transformer1 = TransformCreatureFactory.create_evolved(None, "Super")
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

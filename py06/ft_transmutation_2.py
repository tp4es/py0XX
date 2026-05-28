#!/usr/bin/env	python3
import alchemy.transmutation.recipes


def ft_transmutation():
    try:
        transmutation = alchemy.transmutation.recipes.lead_to_gold()
        print(transmutation)
    except Exception as e:
        print(f"Error found: {e}")


if __name__ == "__main__":
    ft_transmutation()

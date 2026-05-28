#!/usr/bin/env	python3
from alchemy.transmutation.recipes import lead_to_gold


def ft_transmutation():
    try:
        transmutation = lead_to_gold()
        print(transmutation)
    except Exception as e:
        print(f"Error found: {e}")


if __name__ == "__main__":
    ft_transmutation()

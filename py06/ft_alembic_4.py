#!/usr/bin/env python3

import alchemy


def main():
    print("=== Alembic Test ===")
    try:
        print("Creating Air Element:")
        print(alchemy.create_air())
        print("\nCreating Earth Element:")
        element = alchemy.create_earth()
        print(element)
    except AttributeError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()

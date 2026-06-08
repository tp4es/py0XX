#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Alembic Test ===")
    try:
        print("Creating Air Element:")
        print(alchemy.create_air())
        print("\nCreating Earth Element:")
        element: str = alchemy.create_earth()
        print(element)
    except AttributeError as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()

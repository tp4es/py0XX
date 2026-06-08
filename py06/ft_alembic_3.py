#!/usr/bin/env python3

from alchemy.elements import create_air


def main() -> None:
    element: str = create_air()
    print(element)


if __name__ == "__main__":
    main()

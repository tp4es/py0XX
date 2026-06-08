#!/usr/bin/env python3

from alchemy.elements import create_earth


def main() -> None:
    earth: str = create_earth()
    print(earth)


if __name__ == "__main__":
    main()

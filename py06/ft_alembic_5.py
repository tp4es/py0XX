#!/usr/bin/env python3

import alchemy


def main() -> None:
    element: str = alchemy.create_air()
    print(element)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys


def ft_ancient_text():
    if len(sys.argv) != 2:
        print("Uage: ft_ancient_text.py <file>")
        return
    file = sys.argv[1]
    try:
        print("=== Start ===\n")
        f = open(file, "r")
        print(f"Accessing: {f.name}.")
        print(f.read())
        print("\n=== END ===")
        f.close()
    except PermissionError as e:
        print(f"Error_PermisionDenied: {e}")
    except FileNotFoundError as e:
        print(f"Error_FileNotFound: {e}")
    except Exception as e:
        print(f"UndefinedError: {e}")


if __name__ == "__main__":
    ft_ancient_text()

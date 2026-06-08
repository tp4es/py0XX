#!/usr/bin/env python3

import sys


def original_file(file: str) -> None:
    try:
        print("=== Start ===\n")
        f = open(file, "r")
        print(f"Accessing: {f.name}.")
        print(f.read())
        print("\n=== END Original_File ===")
        f.close()
    except PermissionError as e:
        print(f"Error_PermisionDenied: {e}")
    except FileNotFoundError as e:
        print(f"Error_FileNotFound: {e}")
    except Exception as e:
        print(f"UndefinedError: {e}")


def transformed_file(file: str) -> None:
    try:
        print("\n=== Transform DATA ===\n")
        f = open(file, "r")
        lines = f.readlines()
        f.close()
        nlines = list()
        for line in lines:
            line = line.rstrip("\n") + "#\n"
            nlines.append(line)
            print(line)
        nfile_name = input("Enter new file name (or empty):")
        if nfile_name:
            wf = open(nfile_name, "w")
            wf.writelines(nlines)
            print(f"Saving DATA to '{nfile_name}'")
            wf.close()
            print(f"DATA saved to {nfile_name}")
        else:
            print("¡Not Saving DATA!")
    except PermissionError as e:
        print(f"Error_PermisionDenied: {e}")
    except FileNotFoundError as e:
        print(f"Error_FileNotFound: {e}")
    except Exception as e:
        print(f"UndefinedError: {e}")


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file = sys.argv[1]
    original_file(file)
    transformed_file(file)


if __name__ == "__main__":
    ft_archive_creation()

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
        sys.stderr.write(f"Error_PermisionDenied: {e}")
    except FileNotFoundError as e:
        sys.stderr.write(f"Error_FileNotFound: {e}")
    except Exception as e:
        sys.stderr.write(f"UndefinedError: {e}")


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
        nfile_name = input("\nEnter new file name (or empty): ").strip()
        if nfile_name:
            wf = open(nfile_name, "w")
            wf.writelines(nlines)
            print(f"Saving DATA to '{nfile_name}'")
            wf.close()
            print(f"DATA saved to {nfile_name}")
        else:
            print("¡Not Saving DATA!")
    except PermissionError as e:
        sys.stderr.write(f"Error_PermisionDenied: {e}")
    except FileNotFoundError as e:
        sys.stderr.write(f"Error_FileNotFound: {e}")
    except IsADirectoryError as e:
        sys.stderr.write(f"Error_DirectoryName: {e}")
    except Exception as e:
        sys.stderr.write(f"UndefinedError: {e}")
    try:
        print("Enter new file name (or empty):")
        nfile_name = sys.stdin.readline().rstrip("\n")
        print(nfile_name)
        if nfile_name:
            wf = open(nfile_name, "w")
            wf.writelines(nlines)
            print(f"Saving DATA to '{nfile_name}'")
            wf.close()
            print(f"DATA saved to {nfile_name}")
    except PermissionError as e:
        sys.stderr.write(f"Error_PermisionDenied: {e}")
    except Exception as e:
        sys.stderr.write(f"UndefinedError: {e}")


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file = sys.argv[1]
    original_file(file)
    transformed_file(file)


if __name__ == "__main__":
    ft_stream_management()

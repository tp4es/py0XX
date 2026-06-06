#!/usr/bin/env python3
import sys


def ft_command_quest() -> None:
    lenght: int = len(sys.argv)
    sys_list = sys.argv
    if lenght < 1:
        return
    print(f"Program's name: {sys_list[0]}")
    if lenght == 1:
        print("No aditional arguments provided...")
    for i in range(1, lenght):
        print(f"Argument_V {i} == {sys.argv[i]}")


if __name__ == "__main__":
    ft_command_quest()

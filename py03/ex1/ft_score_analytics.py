#!/usr/bin/env python3
import sys


class GamingError(Exception):
    pass


class ArgumentsCountError(GamingError):
    def __init__(
            self,
            msg="¡¡¡ Insuficient arguments provided, +2 scores required. !!!"):
        self.msg = msg
        super().__init__(msg)


class ArgumentsNonNumeric(GamingError):
    def __init__(
            self,
            msg="¡¡¡ Incorrect Arguments INPUT, Type INT required. !!!"):
        self.msg = msg
        super().__init__(msg)


def count_arguments(lenght: int):
    if lenght < 2:
        raise ArgumentsCountError


def check_arguments(arg):
    try:
        return int(arg)
    except Exception as e:
        raise ArgumentsNonNumeric from e


def ft_score_analytics():
    lenght: int = len(sys.argv)
    my_list = list()
    error_list = list()

    try:
        count_arguments(lenght)
        for i in range(1, lenght):
            try:
                my_list.append(check_arguments(sys.argv[i]))
            except Exception as e:
                error_list.append(e)
    except Exception as e:
        error_list.append(e)
    if len(my_list) >= 2:
        print(f"Scores: {my_list}")
        print(f"Total Active players = {len(my_list)}")
        print(f"Total Score = *** {sum(my_list)} ***")
        print(f"High Score = *** ¡{max(my_list)}! ***")
        print(f"Average Score = *** {int(sum(my_list) / (lenght - 1))} ***")
        print(f"Low Score = __{min(my_list)}__")
        print(
            f"Range from MIN to MAX Score: *** {
                int(max(my_list) - min(my_list))} ***")
    if len(error_list) >= 1:
        print(f"Errors log: {error_list}")


if __name__ == "__main__":
    ft_score_analytics()

import math
from typing import List, Tuple


class GamingError(Exception):
    pass


class ArgumentsNonNumeric(GamingError):
    def __init__(self, entry: str) -> None:
        self.entry = entry
        super().__init__(
            f"¡¡¡ Incorrect Argument INPUT '{entry}', Type INT required. !!!"
        )


def check_arguments(arg: str) -> int:
    try:
        return int(arg)
    except Exception as e:
        raise ArgumentsNonNumeric(arg) from e


log_error: List[Exception] = []


def get_player_pos() -> Tuple[int, int, int]:
    while True:
        raw = input("Introduce coordinates as INTEGER (x,y,z): ")
        parts: List[str] = raw.split(",")
        temp_list: List[int] = []

        for part in parts:
            try:
                print(f"Test SPLIT: {parts}")
                temp_list.append(check_arguments(part.strip()))
                if len(temp_list) == 3:
                    # return a fixed-length tuple
                    return (temp_list[0], temp_list[1], temp_list[2])
            except Exception as e:
                log_error.append(e)
                print(f"Error Caught: {e}")
                break


def ft_coordinate_system() -> None:
    print("First set of Coordinates...")
    player_pos: Tuple[int, int, int] = get_player_pos()
    center_field: Tuple[int, int, int] = (0, 0, 0)
    print(f"Coordinates as tuple: {player_pos}\n")
    print(
        f"X Coordinate: {player_pos[0]}, "
        f"Y Coordinate: {player_pos[1]}, Z Coordinate: {player_pos[2]}"
    )
    distance1: float = math.dist(player_pos, center_field)
    print(f"Player1 distance to the CENTER: {distance1:.2f}")
    print("\nSecond Player set of Coordinates...")
    player2_pos: Tuple[int, int, int] = get_player_pos()
    print(f"Coordinates as tuple: {player2_pos}\n")
    print(
        f"X Coordinate: {player2_pos[0]}, "
        f"Y Coordinate: {player2_pos[1]}, Z Coordinate: {player2_pos[2]}"
    )
    distance2: float = math.dist(player2_pos, center_field)
    print(f"Distance between (Player1:Player2) : {distance2:.2f}")


if __name__ == "__main__":
    ft_coordinate_system()

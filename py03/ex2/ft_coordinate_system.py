#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_coordinate_system.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tide-oli <marvin@42.fr>                   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/17 14:26:59 by tide-oli        #+#    #+#               #
#  Updated: 2026/04/17 18:25:37 by tide-oli        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import math


class GamingError(Exception):
    pass


class ArgumentsNonNumeric(GamingError):
    def __init__(self, entry):
        self.entry = entry
        super().__init__(
            f"¡¡¡ Incorrect Argument INPUT '{entry}', Type INT required. !!!")


def check_arguments(arg):
    try:
        return int(arg)
    except Exception as e:
        raise ArgumentsNonNumeric(arg) from e


log_error = list()


def get_player_pos():
    pos_tuple = tuple()
    temp_list = list()

    while True:
        args = input("Introduce coordinates as INTEGER (x,y,z): ")
        args = args.split(",")
        for i in range(len(args)):
            try:
                print(f"Test SPLIT: {args}")
                temp_list.append(check_arguments(args[i].strip()))
                if len(temp_list) == 3:
                    pos_tuple = tuple(temp_list)
                    break
            except Exception as e:
                log_error.append(e)
                print(f"Error Caught: {e}")
                break
            finally:
                temp_list.clear()
        if len(pos_tuple) == 3:
            return pos_tuple


def ft_coordinate_system():
    print("First set of Coordinates...")
    player_pos = get_player_pos()
    center_field = (0, 0, 0)
    print(f"Coordinates as tuple: {player_pos}\n")
    print(
        f"X Coordinate: {
            player_pos[0]}, Y Coordinate: {
            player_pos[1]}, Z Coordinate: {
                player_pos[2]}")
    distance = math.dist(player_pos, center_field)
    print(f"Player1 distance to the CENTER: {distance:.2f}")
    print("\nSecond Player set of Coordinates...")
    player2_pos = get_player_pos()
    print(f"Coordinates as tuple: {player2_pos}\n")
    print(
        f"X Coordinate: {
            player2_pos[0]}, Y Coordinate: {
            player2_pos[1]}, Z Coordinate: {
                player2_pos[2]}")
    distance = math.dist(player2_pos, center_field)
    print(f"Distance between (Player1:Player2) : {distance:.2f}")


if __name__ == "__main__":
    ft_coordinate_system()

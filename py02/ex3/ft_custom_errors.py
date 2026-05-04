#!/usr/bin/env python3

class Plants:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class GardenError(Exception):
    pass


class PlantError (GardenError):
    def __init__(self, msg="Default PlantError!!!"):
        self.msg = msg
        super().__init__(msg)


class WaterError (GardenError):
    def __init__(self, msg="Default WaterError!!!"):
        self.msg = msg
        super().__init__(msg)


def plant_error_test(input):
    try:
        return int(input)
    except Exception:
        raise PlantError


def water_error_test(input):
    try:
        return int(input)
    except Exception:
        raise WaterError


def ft_custom_errors():
    print("=== Testing Self ErrorHandler")
    print("Testing PlantError...")
    try:
        plant_error_test("a")
    except PlantError as e:
        print(f"When not edited PlantError shows: {e}\n")
    print("Testing WaterError...")
    try:
        water_error_test("a")
    except WaterError as e:
        print(f"When not edited PlantError shows: {e}\n")
    print("Testing GardeError...")
    try:
        plant_error_test("a")
    except GardenError:
        print("When called as GardenError\n")
    print("Testing WaterError...")
    try:
        water_error_test("a")
    except GardenError:
        print("When called as GardenError.\n")
    print("Still running...")


if __name__ == "__main__":
    ft_custom_errors()

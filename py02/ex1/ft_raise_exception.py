#!/usr/bin/env python3

def input_temperature(temp: str):
    try:
        n = int(temp)
    except ValueError:
        raise ValueError(
            "Invalid temperature input. Please enter a valid integer.")
    if n not in range(0, 41):
        raise ValueError(
            "Temperature must be between 0 and 40 degrees Celsius.")
    return n


def test_temperature():
    value1: str = "30"
    value2: str = "30a"
    value3: str = "-100"
    value4: str = "50"
    temp: int = 0

    print("=== Garden Temperature ===\n")
    test_list = [value1, value2, value3, value4]
    for value in test_list:
        print(f"Input data is '{value}'")
        try:
            temp = input_temperature(value)
            print(f"New Temperature: {temp}°C\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    print("Program continues running...")


def ft_raise_exception():
    test_temperature()


if __name__ == "__main__":
    ft_raise_exception()

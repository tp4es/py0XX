#!/usr/bin/env python3

def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    print("=== Test 1: Valid input ===")
    try:
        temp = input_temperature("25")
        print(f"New Temperature: {temp}°C")
    except ValueError:
        print("Error: invalid temperature")

    print("\n=== Test 2: Invalid input ===")
    try:
        temp = input_temperature("abc")
        print(f"New Temperature: {temp}°C")
    except ValueError:
        print("Error: invalid temperature")

    print("\nProgram continues running...")


def ft_first_exception():
    test_temperature()


if __name__ == "__main__":
    ft_first_exception()

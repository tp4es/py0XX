def ft_garden_intro() -> None:
    name: str = "rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to the Garden! ===")
    print(
        f"\nPlant: {name.capitalize()}\n"
        f"Height: {str(height)}cm\nAge: {str(age)} days\n")
    print("=== End of PROGRAM! ===")


if __name__ == "__main__":
    ft_garden_intro()

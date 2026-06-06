def ft_count_harvest_recursive() -> None:
    harvest = int(input("Days until harvest: "))

    def recursive(harvest: int) -> None:
        if harvest > 1:
            recursive(harvest - 1)
        print(f"Day {harvest}")
    recursive(harvest)

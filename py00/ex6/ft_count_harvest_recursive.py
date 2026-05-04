def ft_count_harvest_recursive():
    harvest = int(input("Days until harvest: "))

    def recursive(harvest):
        if harvest > 1:
            recursive(harvest - 1)
        print(f"Day {harvest}")
    recursive(harvest)

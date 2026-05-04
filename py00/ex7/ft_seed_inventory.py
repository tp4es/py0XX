units = ["packets", "grams", "area"]
unit_format = [" avaiable", " total", ""]


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit not in units:
        print("Unknown unit type")
        return
    print((f"{seed_type.capitalize()} seeds: {quantity} {unit}{
        unit_format[units.index(unit)]}."))

import alchemy
from elements import create_fire


def lead_to_gold() -> str:
    return (
        "Recibe transmuting Lead to Gold: "
        f"brew '{alchemy.create_air()}' and '{alchemy.original_strength()}' mixed with "
        f"{create_fire()}"
    )

#!/usr/bin/env python3
import sys
from typing import Dict, List, Sequence


inventory: Dict[str, int] = {}


class InventorySystemError(Exception):
    pass


class InventoryRedudantError(InventorySystemError):
    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"Item '{value}', already exist.")


class InventoryInvalidEntrance(InventorySystemError):
    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(
            f"Incorrect DATA Format: {value}. Required <item_name>:<Qty>."
        )


def parser(entry: Sequence[str]) -> List[str]:
    errors: List[str] = []

    for a in entry[1:]:
        clean = (a.replace("<", "").replace(">", ""))
        splitted = clean.split(",")
        for x in splitted:
            pair = x.strip()
            if not pair:
                continue
            try:
                if ":" not in pair:
                    raise InventoryInvalidEntrance(
                        f"'{pair}' missing ':' separator"
                    )
                name, qty = pair.split(":", 1)
                name = name.strip()
                qty = qty.strip()
                if not name:
                    raise InventoryInvalidEntrance(f"'{pair}' has empty name")
                if not qty.isdigit():
                    raise InventoryInvalidEntrance(
                        f"'{pair}' has invalid quantity '{qty}'"
                    )
                add_inventory(name, int(qty))
            except (InventoryInvalidEntrance, InventoryRedudantError) as e:
                errors.append(str(e))
    return errors


def add_inventory(name: str, qty: int) -> None:
    if name in inventory:
        raise InventoryRedudantError(name)
    inventory[name] = int(qty)


def ft_inventory_system() -> None:
    try:
        errors = parser(sys.argv)
        if errors:
            for error in errors:
                print(f"Error: {error}")
    except Exception as e:
        print(f"Error: {e}")
    print(f"===\n\nGot Inventory: \n{inventory}")
    print(f"\nItem list: {list(inventory.keys())}")
    total_items = sum(inventory.values())
    print(f"Total quantity of items = {total_items}")
    if inventory and total_items > 0:
        for item in inventory:
            pct = round(inventory[item] / total_items * 100)
            print(f"\nItem {item}, represents {pct}%")
        max_item = max(inventory, key=lambda k: inventory[k])
        min_item = min(inventory, key=lambda k: inventory[k])
        print(f"\nMost abundant {max_item}, qty = {inventory[max_item]}")
        print(f"Least abundant {min_item}, qty = {inventory[min_item]}")
    else:
        print("\nMost abundant: N/A")
        print("Least abundant: N/A")


if __name__ == "__main__":
    ft_inventory_system()

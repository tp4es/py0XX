from .dark_spellbook import elements_list


def validate_ingredients(ingredients: str) -> str:
    for element in elements_list:
        if ingredients.__contains__(element):
            return (ingredients + ": VALID")
    return (ingredients + "INVALID")

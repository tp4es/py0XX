elements_list = ['earth', 'air', 'fire', 'water']


def validate_ingredients(ingredients: str) -> str:
    for element in elements_list:
        if ingredients.__contains__(element):
            return (ingredients + ": VALID")
    return (ingredients + "INVALID")

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    elements_list: list[str] = light_spell_allowed_ingredients()
    for element in elements_list:
        if ingredients.__contains__(element):
            return (ingredients + ": VALID")
    return (ingredients + "INVALID")

from .dark_validator import validate_ingredients

elements_list = ['bats', 'frogs', 'arsenic', 'eyeball']


def dark_spell_allowed_ingredients() -> list:
    return (elements_list)


def dark_spell_record(spell_name: str, ingredients: str):
    try:
        if (validate_ingredients(ingredients).__contains__("INVALID")):
            return ("Spell Rejected")
        return (f"Spell named {spell_name} Recorded")
    except Exception as e:
        print(f"Error Found: {e}")

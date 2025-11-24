def recipes(filename: str) -> dict:
    recipe_list = {}

    with open(filename) as file:
        contents = file.read()

        for recipe in contents.split("\n\n"):
            name, prep_time, *ingredients = recipe.split("\n")

            recipe_list[name] = {
                "prep_time": int(prep_time),
                "ingredients": [
                    ingredient.strip() for ingredient in ingredients if ingredient
                ],
            }

    return recipe_list


def search_by_name(filename: str, word: str):
    return [
        recipe_name for recipe_name in recipes(filename) if word in recipe_name.lower()
    ]


def search_by_time(filename: str, prep_time: int):
    return [
        f"{recipe_name}, preparation time {recipe.get('prep_time')} min"
        for recipe_name, recipe in recipes(filename).items()
        if recipe.get("prep_time") <= prep_time
    ]


def search_by_ingredient(filename: str, ingredient: str):
    return [
        f"{recipe_name}, preparation time {recipe['prep_time']} min"
        for recipe_name, recipe in recipes(filename).items()
        if ingredient in recipe.get("ingredients", [])
    ]

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes(reqests, dish):
    servings = int(reqests.GET.get('servings', 1))
    recipe = {}
    for ingrident, amount in DATA[dish].items():
        recipe.update({ingrident: round(servings * amount, 2)})

    context = {'recipe': recipe}

    return render(reqests, "calculator/index.html", context)

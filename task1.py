if __name__ == '__main__':
    ingredients = ["hleb", "pomidor", "mascorpone", "mayanez"]
    i = 0
    while i != len(ingredients):
        ingredient = ingredients[i]
        i += 1
        print(ingredient)

    for ingredient in ingredients:
        print(i, ingredient)
def get_input(filename):
    with open(filename) as file:
        return file.readlines()


def get_ingredients(filename):
    data = get_input(filename)

    ingredients = []
    for i in data:
        tmp1 = i.split(" ")
        name = tmp1[0][:-1]
        ingredients.append(
            [int(tmp1[2][:-1]),
             int(tmp1[4][:-1]),
             int(tmp1[6][:-1]),
             int(tmp1[8][:-1]),
             int(tmp1[10])])

    return ingredients

def get_input(filename):
    with open(filename) as file:
        return file.readlines()


def ticker_tape():
    ticker = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    return ticker


def aunt_list(filename):
    data = get_input(filename)
    aunties = []

    for i in data:
        tmp = i.split(" ")
        aunt = tmp[1][:-1]
        item1, qty1 = tmp[2][:-1], int(tmp[3][:-1])
        item2, qty2 = tmp[4][:-1], int(tmp[5][:-1])
        item3, qty3 = tmp[6][:-1], int(tmp[7])

        aunties.append([aunt, item1, qty1, item2, qty2, item3, qty3])

    return aunties


def part2_checker(item, qty, ticker):
    match = False
    if (item == "cats") or (item == "trees"):
        if qty > ticker:
            match = True
    elif (item == "pomeranians") or (item == "goldfish"):
        if qty < ticker:
            match = True
    else:
        match = (ticker == qty)

    return match

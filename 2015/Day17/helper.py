from itertools import combinations


def get_input(filename):
    with open(filename) as file:
        tmp = file.readlines()
    new_tmp = []
    for i in tmp:
        new_tmp.append(int(i.strip()))
    return new_tmp


def test():
    data = [20, 15, 10, 5, 5]
    return data


def combs(data, i):
    return combinations(data, i)

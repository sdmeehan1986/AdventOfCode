def get_input(filename):
    with open(filename) as file:
        tmp = file.readlines()
    new_tmp = []
    for i in tmp:
        new_tmp.append(i.strip())
    return new_tmp


def data_parser(data):
    data_dict = {}
    for i in data:
        tmp = i.split(" ")
        loc1, loc2, dist = tmp[0], tmp[2], tmp[4]

        if loc1 not in data_dict.keys():
            data_dict[loc1] = {loc2: int(dist)}
        else:
            data_dict[loc1][loc2] = int(dist)

        if loc2 not in data_dict.keys():
            data_dict[loc2] = {loc1: int(dist)}
        else:
            data_dict[loc2][loc1] = int(dist)
    return data_dict


def distances(data_dict, routes):
    longest = 0
    shortest = 1000000
    for route in routes:
        dist = 0
        for i in range(len(route) - 1):
            dist += data_dict[route[i]][route[i + 1]]
        if dist > longest:
            longest = dist
        if dist < shortest:
            shortest = dist

    return [longest, shortest]

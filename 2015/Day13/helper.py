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
        member1, member2, change, value = tmp[0], tmp[10][:-1], tmp[2], tmp[3]

        if change == "lose":
            change = 0 - int(value)
        else:
            change = int(value)

        if member1 not in data_dict.keys():
            data_dict[member1] = {member2:change}
        else:
            data_dict[member1][member2] = change

    return data_dict


def get_happiness(table, members):
    happiness = {}
    i = 0

    while i < len(table):
        if i == 0:
            tmpa = members[table[i]][table[i + 1]]
            tmpb = members[table[i]][table[len(table) - 1]]
            happiness[table[i]] = tmpa + tmpb
        elif i == len(table)-1:
            tmpa = members[table[i]][table[0]]
            tmpb = members[table[i]][table[i - 1]]
            happiness[table[i]] = tmpa + tmpb
        else:
            tmpa = members[table[i]][table[i + 1]]
            tmpb = members[table[i]][table[i - 1]]
            happiness[table[i]] = tmpa + tmpb
        i += 1

    table_happy = 0
    for mem in happiness.keys():
        table_happy += happiness[mem]

    return table_happy

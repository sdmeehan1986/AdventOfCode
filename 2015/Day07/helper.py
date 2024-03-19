def get_input(filename):
    with open(filename) as file:
        temp = file.readlines()
    new_temp = []
    for i in temp:
        new_temp.append(i.strip())
    return new_temp


def bit_and(in_a, in_b, out, dic):
    a, b = 0, 0
    if in_a.isdigit():
        a = int(in_a)
    else:
        a = dic[in_a]

    if in_b.isdigit():
        b = int(in_b)
    else:
        b = dic[in_b]

    to_add = a & b
    if to_add < 0:
        to_add += 65536

    dic[out] = to_add
    return dic


def bit_or(in_a, in_b, out, dic):
    a, b = 0, 0
    if in_a.isdigit():
        a = int(in_a)
    else:
        a = dic[in_a]

    if in_b.isdigit():
        b = int(in_b)
    else:
        b = dic[in_b]

    to_add = a | b
    if to_add < 0:
        to_add += 65536

    dic[out] = to_add
    return dic


def bit_left(in_a, in_b, out, dic):
    a, b = 0, 0
    if in_a.isdigit():
        a = int(in_a)
    else:
        a = dic[in_a]

    if in_b.isdigit():
        b = int(in_b)

    to_add = a << b
    if to_add < 0:
        to_add += 65536

    dic[out] = to_add
    return dic


def bit_right(in_a, in_b, out, dic):
    a, b = 0, 0
    if in_a.isdigit():
        a = int(in_a)
    else:
        a = dic[in_a]

    if in_b.isdigit():
        b = int(in_b)

    to_add = a >> b
    if to_add < 0:
        to_add += 65536

    dic[out] = to_add
    return dic


def bit_not(in_a, out, dic):
    a, b = 0, 0
    if in_a.isdigit():
        a = int(in_a)
    else:
        a = dic[in_a]

    to_add = ~a
    if to_add < 0:
        to_add += 65536

    dic[out] = to_add
    return dic


def in_signal(signal, wire, dic):

    if signal.isdigit():
        signal = int(signal)
    else:
        signal = dic[signal]

    dic[wire] = signal
    return dic

def get_input(filename):
    with open(filename) as file:
        tmp = file.readlines()
    new_tmp = []
    for i in tmp:
        new_tmp.append(i.strip())
    return new_tmp


def stats(data):
    racers = {}

    for i in data:
        tmp = i.split(" ")
        raindeer = tmp[0]
        speed = int(tmp[3])
        time = int(tmp[6])
        rest = int(tmp[13])

        racers[raindeer] = {"speed": speed, "time": time, "rest": rest}

    return racers


def race(raindeer, speed, time, rest, distance):
    total = 0
    multiplier = distance // (time + rest)
    remainder = distance % (time + rest)
    total += speed * time * multiplier

    if remainder != 0:
        if remainder > time:
            total += speed * time
        else:
            total += remainder * speed

    return total

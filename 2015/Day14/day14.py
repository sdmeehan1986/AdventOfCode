import helper


def part1(filename, distance):
    data = helper.get_input(filename)
    racers = helper.stats(data)
    raced = []

    for i in racers:
        raindeer = i
        speed = racers[i]["speed"]
        time = racers[i]["time"]
        rest = racers[i]["rest"]
        traveled = helper.race(raindeer, speed, time, rest, distance)
        raced.append([raindeer, traveled])

    winner = ''
    dist = 0
    for i in raced:
        tmp1, tmp2 = i
        if tmp2 > dist:
            winner = tmp1
            dist = tmp2
    print(f'The winner of the race is {winner}, with a total traveled distance of {dist}')


def part2(filename, distance):
    data = helper.get_input(filename)
    racers = helper.stats(data)
    raced = {}
    for i in racers:
        raced[i] = {"traveled": 0, "points": 0}

    for rounds in range(1, distance+1):
        leader = 0
        for raindeer in racers:
            speed = racers[raindeer]["speed"]
            time = racers[raindeer]["time"]
            rest = racers[raindeer]["rest"]
            traveled = helper.race(raindeer, speed, time, rest, rounds)
            raced[raindeer]["traveled"] = traveled
            if traveled > leader:
                leader = traveled
        for j in raced:
            if raced[j]["traveled"] == leader:
                raced[j]["points"] += 1

    print(raced)
    winner = ''
    points = 0
    for raindeer in raced:
        tmp1 = raced[raindeer]["points"]
        if tmp1 > points:
            winner = raindeer
            points = tmp1
    print(f'The winner of the race is {winner}, with a total points of {points}')


print("=======================================================")
print("Starting test run for part 1.")
part1("test_input.txt", 1000)
print("=======================================================\n")

print("=======================================================")
print("Starting live run for part 1.")
part1("input.txt", 2503)
print("=======================================================\n")

print("=======================================================")
print("Starting test run for part 2.")
part2("test_input.txt", 1000)
print("=======================================================\n")

print("=======================================================")
print("Starting live run for part 2.")
part2("input.txt", 2503)
print("=======================================================\n")

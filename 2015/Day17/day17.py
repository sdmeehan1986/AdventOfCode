import helper


def part1a(data, liters):
    found = 0
    containers = 21

    for i in range(len(data)):
        tmp = 0
        combo = helper.combs(data, i)
        for j in combo:
            if sum(j) == liters:
                tmp += 1
                if len(j) < containers:
                    containers = len(j)
        found += tmp
    return [found, containers]


print("=================================")
print("Starting test run for part 1.")
found, containers = part1a(helper.test(), 25)
print(f'The number of combinations found is {found}, with least number of containers at {containers}')
print("=================================\n")

print("=================================")
print("Starting live run for part 1.")
data = helper.get_input("input.txt")
found, containers = part1a(data, 150)
print(f'The number of combinations found is {found}, with least number of containers at {containers}')
print("=================================\n")

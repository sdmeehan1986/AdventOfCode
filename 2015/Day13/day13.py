from itertools import permutations
import helper


def part1(members):
    tables = permutations(members)
    happiness = 0

    for table in tables:
        tmp = helper.get_happiness(table, members)
        if tmp > happiness:
            happiness = tmp
    print(f'Happiest table has a value of {happiness}')


def part2(members):
    data = []
    for i in members.keys():
        data.append(i)

    for i in data:
        if "Stefan" not in members.keys():
            members["Stefan"] = {i: 0}
            members[i]["Stefan"] = 0
        else:
            members["Stefan"][i] = 0
            members[i]["Stefan"] = 0

    tables = permutations(members)
    happiness = 0

    for table in tables:
        tmp = helper.get_happiness(table, members)
        if tmp > happiness:
            happiness = tmp
    print(f'Happiest table has a value of {happiness}')


print("=============================================")
print("Running test which should output a value of 330")
data = helper.data_parser(helper.get_input(("test_input.txt")))
part1(data)
print("=============================================\n")

print("=============================================")
print("Running part 1 live")
data = helper.data_parser(helper.get_input(("input.txt")))
part1(data)
print("=============================================\n")

print("=============================================")
print("Running part 2 live")
data = helper.data_parser(helper.get_input(("input.txt")))
part2(data)
print("=============================================\n")

import json


def get_data(filename):
    with open(filename)as file:
        data = json.load(file)
        return data


def is_dict(data, ignore):
    count = 0
    red = False

    if ignore:
        for i, j in data.items():
            if j == "red":
                return 0
            elif isinstance(j, dict):
                count += is_dict(j, ignore)
            elif isinstance(j, list):
                count += is_list(j, ignore)
            elif isinstance(j, int):
                count += j

    elif not ignore:
        for i, j in data.items():
            if isinstance(j, dict):
                count += is_dict(j, ignore)
            elif isinstance(j, list):
                count += is_list(j, ignore)
            elif isinstance(j, int):
                count += j

    return count


def is_list(data, ignore):
    count = 0
    for i in data:
        if isinstance(i, dict):
            count += is_dict(i,ignore)
        elif isinstance(i, list):
            count += is_list(i, ignore)
        elif isinstance(i, int):
            count += i
    return count


def get_numbers(data, ignore):
    count = 0

    if isinstance(data, dict):
        count += is_dict(data, ignore)

    return count


print("=============================")
print("Starting live run part 1")
data = get_data("input.txt")
numbers = get_numbers(data, False)
print(numbers)
print("=============================\n")
print("=============================")
print("Starting live run part 2")
numbers = get_numbers(data, True)
print(numbers)
print("=============================\n")

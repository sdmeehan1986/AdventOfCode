def get_input(file_name):
    with open(file_name) as file:
        return file.readlines()


def sides(data):
    return [int(x.rstrip()) for x in data.split("x")]


def test():
    print("Starting test run 1")
    data = get_input("test.txt")
    total = 0
    ribbon = 0

    for i in data:
        l, w, h = sides(i)
        area = [l * w, w * h, h * l]
        smallest = area
        smallest.sort()
        total += sum([x * 2 for x in area]) + smallest[0]

        check = [l, w, h]
        check.sort()
        first = check[0]
        second = check[1]
        ribbon += (first * 2) + (second * 2) + (l * w * h)

    print(f'The total wrapping paper required is {total}')
    print(f'The total ribbon required is {ribbon}')
    print("---------------")


def live():
    print("Starting live run 1")
    data = get_input("input.txt")
    total = 0
    ribbon = 0
    for i in data:
        l, w, h = sides(i)
        area = [l * w, w * h, h * l]
        smallest = area
        smallest.sort()
        total += sum([x * 2 for x in area]) + smallest[0]

        check = [l, w, h]
        check.sort()
        first = check[0]
        second = check[1]
        ribbon += (first * 2) + (second * 2) + (l * w * h)

    print(f'The total wrapping paper required is {total}')
    print(f'The total ribbon required is {ribbon}')
    print("---------------")


test()
live()

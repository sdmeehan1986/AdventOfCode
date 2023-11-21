def get_input(file_name):
    with open(file_name) as file:
        return file.read()

def test():
    print("Starting test")
    instructions = "^>v<"
    location = [0, 0]
    visited = [(0, 0)]
    for i in instructions:
        if i == "^":
            x, y = location
            location = [x, y + 1]
            visited.append((x, y + 1))
        if i == ">":
            x, y = location
            location = [x + 1, y]
            visited.append((x + 1, y))
        if i == "v":
            x, y = location
            location = [x, y - 1]
            visited.append((x, y - 1))
        if i == "<":
            x, y = location
            location = [x - 1, y]
            visited.append((x - 1, y))
    unique = set(visited)
    print(f'The number of unique houses visited are {len(unique)}')
    print("----------------")

def live():
    print("Starting live")
    instructions = get_input("input.txt")
    location = [0, 0]
    visited = [(0, 0)]
    for i in instructions:
        if i == "^":
            x, y = location
            location = [x, y + 1]
            visited.append((x, y + 1))
        if i == ">":
            x, y = location
            location = [x + 1, y]
            visited.append((x + 1, y))
        if i == "v":
            x, y = location
            location = [x, y - 1]
            visited.append((x, y - 1))
        if i == "<":
            x, y = location
            location = [x - 1, y]
            visited.append((x - 1, y))
    unique = set(visited)
    print(f'The number of unique houses visited are {len(unique)}')
    print("----------------")

def test2():
    print("Starting test 2")
    instructions = "^>v<"
    santas = [[0, 0], [0, 0]]
    visited = [(0, 0), (0, 0)]
    routes = [instructions[::2], instructions[1::2]]

    for j in range(0, 2):
        for i in routes[j]:
            if i == "^":
                x, y = santas[j]
                santas[j] = [x, y + 1]
                visited.append((x, y + 1))
            if i == ">":
                x, y = santas[j]
                santas[j] = [x + 1, y]
                visited.append((x + 1, y))
            if i == "v":
                x, y = santas[j]
                santas[j] = [x, y - 1]
                visited.append((x, y - 1))
            if i == "<":
                x, y = santas[j]
                santas[j] = [x - 1, y]
                visited.append((x - 1, y))
    unique = set(visited)
    print(f'The number of unique houses visited are {len(unique)}')
    print("----------------")

def live2():
    print("Starting live 2")
    instructions = get_input("input.txt")
    santas = [[0, 0], [0, 0]]
    visited = [(0, 0), (0, 0)]
    routes = [instructions[::2], instructions[1::2]]

    for j in range(0, 2):
        for i in routes[j]:
            if i == "^":
                x, y = santas[j]
                santas[j] = [x, y + 1]
                visited.append((x, y + 1))
            if i == ">":
                x, y = santas[j]
                santas[j] = [x + 1, y]
                visited.append((x + 1, y))
            if i == "v":
                x, y = santas[j]
                santas[j] = [x, y - 1]
                visited.append((x, y - 1))
            if i == "<":
                x, y = santas[j]
                santas[j] = [x - 1, y]
                visited.append((x - 1, y))
    unique = set(visited)
    print(f'The number of unique houses visited are {len(unique)}')
    print("----------------")


test()
live()
test2()
live2()

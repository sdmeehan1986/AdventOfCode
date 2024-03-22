def test():
    data = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    pos = [1, 1]

    for i in data:
        for move in i:
            # print(move)
            if move == "U":
                # print("moving up")
                if pos[0] > 0:
                    pos[0] -= 1
                # print(pos)
            if move == "D":
                # print("moving down")
                if pos[0] < 2:
                    pos[0] += 1
                # print(pos)
            if move == "L":
                # print("moving left")
                if pos[1] > 0:
                    pos[1] -= 1
                # print(pos)
            if move == "R":
                # print("moving right")
                if pos[1] < 2:
                    pos[1] += 1
                # print(pos)
        print(keypad[pos[0]][pos[1]], end="")
    print("")


def test2():
    data = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    keypad = [[-1, -1, 1, -1, -1], [-1, 2, 3, 4, -1], [5, 6, 7, 8, 9], [-1, "A", "B", "C", -1], [-1, -1, "D", -1, -1]]
    pos = [2, 0]
    print(keypad[pos[0]][pos[1]])

    for i in data:
        for move in i:
            # print(move)
            if move == "U":
                if pos[0] > 0:
                    tmp = keypad[pos[0]-1][pos[1]]
                    if tmp != -1:
                        pos[0] -= 1
                # print(pos)
            if move == "D":
                if pos[0] < 4:
                    tmp = keypad[pos[0] + 1][pos[1]]
                    if tmp != -1:
                        pos[0] += 1
                # print(pos)
            if move == "L":
                if pos[1] > 0:
                    tmp = keypad[pos[0]][pos[1] - 1]
                    if tmp != -1:
                        pos[1] -= 1
                # print(pos)
            if move == "R":
                if pos[1] < 4:
                    tmp = keypad[pos[0]][pos[1] + 1]
                    if tmp != -1:
                        pos[1] += 1
                # print(pos)
        print(keypad[pos[0]][pos[1]], end="")
    print("")


def part1():
    data = open("input/day02.txt").read().split()
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    pos = [1, 1]

    for i in data:
        for move in i:
            # print(move)
            if move == "U":
                # print("moving up")
                if pos[0] > 0:
                    pos[0] -= 1
                # print(pos)
            if move == "D":
                # print("moving down")
                if pos[0] < 2:
                    pos[0] += 1
                # print(pos)
            if move == "L":
                # print("moving left")
                if pos[1] > 0:
                    pos[1] -= 1
                # print(pos)
            if move == "R":
                # print("moving right")
                if pos[1] < 2:
                    pos[1] += 1
                # print(pos)
        print(keypad[pos[0]][pos[1]], end="")
    print("")


def part2():
    data = open("input/day02.txt").read().split()
    keypad = [[-1, -1, 1, -1, -1], [-1, 2, 3, 4, -1], [5, 6, 7, 8, 9], [-1, "A", "B", "C", -1], [-1, -1, "D", -1, -1]]
    pos = [2, 0]
    print(keypad[pos[0]][pos[1]])

    for i in data:
        for move in i:
            # print(move)
            if move == "U":
                if pos[0] > 0:
                    tmp = keypad[pos[0]-1][pos[1]]
                    if tmp != -1:
                        pos[0] -= 1
                # print(pos)
            if move == "D":
                if pos[0] < 4:
                    tmp = keypad[pos[0] + 1][pos[1]]
                    if tmp != -1:
                        pos[0] += 1
                # print(pos)
            if move == "L":
                if pos[1] > 0:
                    tmp = keypad[pos[0]][pos[1] - 1]
                    if tmp != -1:
                        pos[1] -= 1
                # print(pos)
            if move == "R":
                if pos[1] < 4:
                    tmp = keypad[pos[0]][pos[1] + 1]
                    if tmp != -1:
                        pos[1] += 1
                # print(pos)
        print(keypad[pos[0]][pos[1]], end="")
    print("")


test()
part1()
test2()
part2()

def part1(commands, part2=False):
    grid = [0, 0]
    visited = [[0, 0]]

    facing = "North"
    for i in commands:
        turn = i[0:1]
        move = int(i[1:])

        if facing == "North":
            if turn == "R":
                facing = "East"
            elif turn == "L":
                facing = "West"
        elif facing == "East":
            if turn == "R":
                facing = "South"
            elif turn == "L":
                facing = "North"
        elif facing == "South":
            if turn == "R":
                facing = "West"
            elif turn == "L":
                facing = "East"
        elif facing == "West":
            if turn == "R":
                facing = "North"
            elif turn == "L":
                facing = "South"

        breaking = False
        if facing == "North":
            for j in range(move):
                grid[1] += 1
                if part2:
                    tmp = [grid[0], grid[1]]
                    if tmp in visited:
                        breaking = True
                        break
                    else:
                        visited.append(tmp)
        elif facing == "East":
            for j in range(move):
                grid[0] += 1
                if part2:
                    tmp = [grid[0], grid[1]]
                    if tmp in visited:
                        breaking = True
                        break
                    else:
                        visited.append(tmp)
        elif facing == "South":
            for j in range(move):
                grid[1] -= 1
                if part2:
                    tmp = [grid[0], grid[1]]
                    if tmp in visited:
                        breaking = True
                        break
                    else:
                        visited.append(tmp)
        elif facing == "West":
            for j in range(move):
                grid[0] -= 1
                if part2:
                    tmp = [grid[0], grid[1]]
                    if tmp in visited:
                        breaking = True
                        break
                    else:
                        visited.append(tmp)
        if breaking:
            break
    count = (abs(grid[0])) + (abs(grid[1]))

    print(count)


data = open("input/day01.txt").read()
commands = data.split(", ")
part1(commands)
part1(commands, True)
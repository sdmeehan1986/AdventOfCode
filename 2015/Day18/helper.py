import numpy


def get_input(filename):
    with open(filename) as file:
        tmp = file.readlines()
    new_tmp = []
    for i in tmp:
        new_tmp.append(i.strip())
    return new_tmp


def grid_builder(data):
    grid = []
    for i in data:
        tmp = []
        for j in i:
            tmp.append(j)
        grid.append(tmp)

    return numpy.array(grid)


def to_check(x, y, size):
    co_ords = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    check = []

    for i in co_ords:
        if (x == 0) and (i[0] >= 0):
            if (y == 0) and (i[1] >= 0):
                check.append(i)
            elif (y == size - 1) and (i[1] <= 0):
                check.append(i)
            elif (y > 0) and (y < size - 1):
                check.append(i)
        elif (x == size - 1) and (i[0] <= 0):
            if (y == 0) and (i[1] >= 0):
                check.append(i)
            elif (y == size - 1) and (i[1] <= 0):
                check.append(i)
            elif (y > 0) and (y < size - 1):
                check.append(i)
        elif (x > 0) and (x < size - 1):
            if (y > 0) and (y < size - 1):
                check.append(i)
            elif (y == 0) and (i[1] >= 0):
                check.append(i)
            elif (y == size - 1) and (i[1] <= 0):
                check.append(i)

    return check


def update(grid, size, part2):
    new_grid = []
    for row in range(len(grid)):
        x = row
        new_row = []

        for column in range(len(grid[row])):
            y = column
            neighbours_on = 0
            co_ords = to_check(x, y, size)

            for i in co_ords:
                n_x = x+i[0]
                n_y = y+i[1]
                if grid[n_x][n_y] == "#":
                    neighbours_on += 1

            if grid[x][y] == "#":
                if (neighbours_on < 2) or (neighbours_on > 3):
                    new_row.append(".")
                else:
                    new_row.append("#")
            elif grid[x][y] == ".":
                if neighbours_on == 3:
                    new_row.append("#")
                else:
                    new_row.append(".")

        new_grid.append(new_row)

    return new_grid


def counter(grid):
    count = 0
    for i in grid:
        for j in i:
            if j == "#":
                count += 1
    return count


def lights_on(grid, size):
    grid[0][0] = "#"
    grid[size - 1][0] = "#"
    grid[0][size - 1] = "#"
    grid[size - 1][size - 1] = "#"

    return grid

import helper


def part1(filename, runs, size, part2):
    data = helper.get_input(filename)
    grid = helper.grid_builder(data)

    # print(helper.to_check(5, 2, 6))

    for i in range(runs):
        if part2:
            grid = helper.lights_on(grid, size)
        grid = helper.update(grid, size, part2)

    if part2:
        grid = helper.lights_on(grid, size)
    print(f'The number of lights on is {helper.counter(grid)}')


print("=================================")
print("Starting test run for part 1.")
part1("test_input.txt", 4, 6, False)
print("=================================\n")

print("=================================")
print("Starting live run for part 1.")
part1("input.txt", 100, 100, False)
print("=================================\n")

print("=================================")
print("Starting test run for part 2.")
part1("test_input.txt", 5, 6, True)
print("=================================\n")

print("=================================")
print("Starting live run for part 2.")
part1("input.txt", 100, 100, True)
print("=================================\n")

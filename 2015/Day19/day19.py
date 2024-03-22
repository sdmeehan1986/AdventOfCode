import helper


def part1(filename):
    data = helper.get_input(filename)
    replacements, molecule = helper.molecules(data)

    fusion = []
    for r in replacements:
        fusion = helper.fusion(r, molecule[0], fusion)

    unique = set(fusion)
    print(len(unique))


def part2(filename):
    data = helper.get_input(filename)
    replacements, molecule = helper.molecules(data)
    replacements.reverse()

    steps = helper.reverse_engineer(molecule[0], replacements)
    print(steps)


print("=================================")
print("Starting test run for part 1.")
part1("test_input.txt")
print("=================================\n")


print("=================================")
print("Starting live run for part 1.")
part1("input.txt")
print("=================================\n")

print("=================================")
print("Starting test run for part 2.")
part2("test_input.txt")
print("=================================\n")

print("=================================")
print("Starting live run for part 2.")
print("Thanks to users on reddit for explanation of molecular chemistry required for this")
print("https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/")
part2("input.txt")
print("=================================\n")

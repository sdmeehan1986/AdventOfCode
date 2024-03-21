import helper


def part1(filename):
    aunts = helper.aunt_list(filename)
    ticker = helper.ticker_tape()

    for i in aunts:
        aunt, item1, qty1, item2, qty2, item3, qty3 = i

        match1 = (ticker[item1] == qty1)
        match2 = (ticker[item2] == qty2)
        match3 = (ticker[item3] == qty3)

        if match1 and match2 and match3:
            print(f'Aunt number {aunt}, matches the ticker list!!')


def part2(filename):
    aunts = helper.aunt_list(filename)
    ticker = helper.ticker_tape()

    for i in aunts:
        aunt, item1, qty1, item2, qty2, item3, qty3 = i

        match1 = helper.part2_checker(item1, qty1, ticker[item1])
        match2 = helper.part2_checker(item2, qty2, ticker[item2])
        match3 = helper.part2_checker(item3, qty3, ticker[item3])

        if match1 and match2 and match3:
            print(f'Aunt number {aunt}, matches the ticker list!!')


print("=================================")
print("Starting run for part 1.")
part1("input.txt")
print("=================================\n")

print("=================================")
print("Starting run for part 2.")
part2("input.txt")
print("=================================\n")

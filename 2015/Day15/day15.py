import helper


def part1_test(filename, is_part2):
    stats = helper.get_ingredients(filename)
    cookie_score = 0

    for i in range(1, 100):
        j = 100 - i
        cap = stats[0][0]*i + stats[1][0]*j
        dur = stats[0][1]*i + stats[1][1]*j
        fla = stats[0][2]*i + stats[1][2]*j
        tex = stats[0][3]*i + stats[1][3]*j
        cal = stats[0][4]*i + stats[1][4]*j

        if (cal != 500) and is_part2:
            continue
        if not (cap < 0 or dur < 0 or fla < 0 or tex < 0):
            score = cap * dur * fla * tex
            if score > cookie_score:
                cookie_score = score

    return cookie_score


def part1(filename, is_part2):
    stats = helper.get_ingredients(filename)
    cookie_score = 0

    for i in range(1, 100):
        for j in range(1,100 - i):
            for k in range(1, 100 -j):
                h = 100 - i - j - k

                cap = stats[0][0] * i + stats[1][0] * j + stats[2][0] * k + stats[3][0] * h
                dur = stats[0][1] * i + stats[1][1] * j + stats[2][1] * k + stats[3][1] * h
                fla = stats[0][2] * i + stats[1][2] * j + stats[2][2] * k + stats[3][2] * h
                tex = stats[0][3] * i + stats[1][3] * j + stats[2][3] * k + stats[3][3] * h
                cal = stats[0][4] * i + stats[1][4] * j + stats[2][4] * k + stats[3][4] * h

                if (cal != 500) and is_part2:
                    continue
                if not (cap < 0 or dur < 0 or fla < 0 or tex < 0):
                    score = cap * dur * fla * tex
                    if score > cookie_score:
                        cookie_score = score

    return cookie_score


print("=================================")
print("Starting test run for part 1.")
print(f'The best cookie score is {part1_test("test_input.txt", False)}')
print("=================================\n")

print("=================================")
print("Starting live run for part 1.")
print(f'The best cookie score is {part1("input.txt", False)}')
print("=================================\n")

print("=================================")
print("Starting test run for part 2.")
print(f'The best cookie score is {part1_test("test_input.txt", True)}')
print("=================================\n")

print("=================================")
print("Starting live run for part 2.")
print(f'The best cookie score is {part1("input.txt", True)}')
print("=================================\n")

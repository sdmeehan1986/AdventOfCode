def part1(data, reps):
    digits = data

    for runs in range(reps):
        out = ''
        streak = 1
        current = ''
        for i in digits:
            if current == '':
                current = i
            elif i == current:
                streak += 1
            elif i != current:
                out += str(streak) + current
                current = i
                streak = 1
        out += str(streak) + current
        digits = out
    return digits


print("===================")
print("Starting test run 1")
print(part1("1", 5))
print("===================\n")

print("===================")
print("Starting live run 1")
print(len(part1("1113122113", 40)))
print("===================\n")

print("===================")
print("Starting live run 2")
print(len(part1("1113122113", 50)))
print("===================\n")

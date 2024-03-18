def get_input(file_name):
    with open(file_name) as file:
        return file.readlines()


def test():
    print("Starting test run 1")
    test_input = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
    nice = 0

    for i in test_input:
        vowels = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        double = any(a == b for a, b in zip(i, i[1:]))
        clean = "ab" not in i and "cd" not in i and "pq" not in i and "xy" not in i

        if vowels >= 3 and double and clean:
            nice += 1

    print(nice)
    print("========")


def live():
    print("Starting live run 1")
    live_input = get_input("input.txt")
    nice = 0

    for i in live_input:
        vowels = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        double = any(a == b for a, b in zip(i, i[1:]))
        clean = "ab" not in i and "cd" not in i and "pq" not in i and "xy" not in i

        if vowels >= 3 and double and clean:
            nice += 1

    print(nice)
    print("========")


def test2():
    print("Starting test run 2")
    test_input = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
    nice = 0

    for i in test_input:
        two_pair = False
        repeat = False

        j, k = 0, 2
        while k < len(i) + 1:
            partial = i[j:k]
            if i.count(partial) >= 2:
                two_pair = True
                break
            j += 1
            k += 1

        j, k = 0, 3
        while k < len(i) + 1:
            partial = i[j:k]
            if partial[0] == partial[-1]:
                repeat = True
                break
            j += 1
            k += 1

        if two_pair and repeat:
            nice += 1

    print(nice)
    print("========")


def live2():
    print("Starting live run 2")
    live_input = get_input("input.txt")
    nice = 0

    for i in live_input:
        two_pair = False
        repeat = False

        j, k = 0, 2
        while k < len(i) + 1:
            partial = i[j:k]
            if i.count(partial) >= 2:
                two_pair = True
                break
            j += 1
            k += 1

        j, k = 0, 3
        while k < len(i) + 1:
            partial = i[j:k]
            if partial[0] == partial[-1]:
                repeat = True
                break
            j += 1
            k += 1

        if two_pair and repeat:
            nice += 1

    print(nice)
    print("========")


test()
live()
test2()
live2()

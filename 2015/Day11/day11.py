def double_valid(data):
    current = ''
    pairs = 0

    for a in data:
        if current == '':
            current = a
        elif a != current:
            current = a
        elif a == current:
            pairs += 1
            current = ''

    return pairs >= 2


def invalid_letters(data):
    invalid = ["i", "o", "l"]
    is_valid = True

    for i in invalid:
        if i in data:
            is_valid = False

    return is_valid


def three_row(data):
    ordinal = 0
    match = ''
    found = False

    for i in data:
        if ordinal == 0:
            ordinal = ord(i)
            match += i
        elif (ordinal + 1) == ord(i):
            ordinal = ord(i)
            match += i
        elif len(match) >= 3:
            found = True
        else:
            ordinal = ord(i)
            match = i
    return found


def part1(data):
    valid = False
    position = 8
    password = data

    while not valid:
        char = password[position-1:position]
        if ord(char) < 122:
            new_char = chr(ord(char)+1)
            if position < 8:
                password = password[:position - 1] + new_char + password[position:]
            else:
                password = password[:position - 1] + new_char
            position = 8

        if ord(char) == 122:
            if position < 8:
                password = password[:position - 1] + "a" + password[position:]
            else:
                password = password[:position - 1] + "a"
            position -= 1

        if double_valid(password) and invalid_letters(password) and three_row(password):
            break
    return password


print("==============")
print("Running test and output should be 'abcdffaa'")
print(part1("abcdefgh"))
print("==============\n")
print("==============")
print("Running live part 1")
print(part1("hepxcrrq"))
print("==============\n")
print("==============")
print("Running live part 2")
print(part1(part1("hepxcrrq")))
print("==============\n")

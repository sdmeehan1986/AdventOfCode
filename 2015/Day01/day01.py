def get_input(file_name):
    with open(file_name) as file:
        return file.read()

def run1(data):
    print("Starting part 1")
    count = 0
    for i in data:
        if i == "(":
            count +=1
        else:
            count -= 1
    print(count)
    print("-----------")

def run2(data):
    print("Starting part 2")
    char = 0
    reported = False
    count = 0
    for i in data:
        char +=1
        if i == "(":
            count += 1
        else:
            count -= 1
        if count == -1 and not reported:
            reported = True
            print(f'Entered basement floor -1 at point {char}')
    print(count)
    print("-----------")


run1(get_input("input.txt"))
run2(get_input("input.txt"))

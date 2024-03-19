import helper


def test():
    print("Starting test run 1")
    array = helper.builder()
    helper.toggle("499,499", "500,500", array)
    off, on = helper.counter(array)
    print(f'Off is {off}')
    print(f'On is {on}')
    print("==========")


def live():
    print("Starting live run 1")
    array = helper.builder()
    commands = helper.get_input("input.txt")

    for i in commands:
        if i[0:2] == "to":
            splits = i.split(" ")
            helper.toggle(splits[1], splits[3], array)
        else:
            splits = i.split(" ")
            if splits[1] == "off":
                helper.off(splits[2], splits[4], array)
            else:
                helper.on(splits[2], splits[4], array)

    off, on = helper.counter(array)
    print(f'Off is {off}')
    print(f'On is {on}')
    print("==========")


def test2():
    print("Starting test run 2")
    array = helper.builder()
    helper.toggle_p2("499,499", "500,500", array)
    brightness = helper.counter_p2(array)
    print(f'brightness is {brightness}')
    print("==========")


def live2():
    print("Starting live run 2")
    array = helper.builder()
    commands = helper.get_input("input.txt")

    for i in commands:
        if i[0:2] == "to":
            splits = i.split(" ")
            helper.toggle_p2(splits[1], splits[3], array)
        else:
            splits = i.split(" ")
            if splits[1] == "off":
                helper.off_p2(splits[2], splits[4], array)
            else:
                helper.on_p2(splits[2], splits[4], array)

    brightness = helper.counter_p2(array)
    print(f'Brightness is {brightness}')
    print("==========")


test()
live()
test2()
live2()

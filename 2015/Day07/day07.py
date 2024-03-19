import helper


def test():
    print("=============================================")
    print("Starting test run 1")
    commands = helper.get_input("input.txt")
    wires = {}

    while len(commands) > 0:
        next_command = commands.pop(0)
        used = False

        if "AND" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if (optiona.isdigit() or optiona in wires.keys()) and (optionb.isdigit() or optionb in wires.keys()):
                wires = helper.bit_and(optiona, optionb, options[4], wires)
                used = True

        elif "OR" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if (optiona.isdigit() or optiona in wires.keys()) and (optionb.isdigit() or optionb in wires.keys()):
                wires = helper.bit_or(optiona, optionb, options[4], wires)
                used = True

        elif "LSHIFT" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_left(optiona, optionb, options[4], wires)
                used = True

        elif "RSHIFT" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_right(optiona, optionb, options[4], wires)
                used = True
        elif "NOT" in next_command:
            options = next_command.split(" ")
            optiona = options[1]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_not(optiona, options[3], wires)
                used = True
        else:
            options = next_command.split(" ")
            optiona = options[0]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.in_signal(options[0], options[2], wires)
                used = True

        if not used:
            commands.append(next_command)
    print(f'The end has completed with dict of {wires}')
    print("=============================================\n\n")


def live():
    print("=============================================")
    print("Starting live run 1")
    commands = helper.get_input("input.txt")
    wires = {}

    while len(commands) > 0:
        next_command = commands.pop(0)
        used = False

        if "AND" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if (optiona.isdigit() or optiona in wires.keys()) and (optionb.isdigit() or optionb in wires.keys()):
                wires = helper.bit_and(optiona, optionb, options[4], wires)
                used = True

        elif "OR" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if (optiona.isdigit() or optiona in wires.keys()) and (optionb.isdigit() or optionb in wires.keys()):
                wires = helper.bit_or(optiona, optionb, options[4], wires)
                used = True

        elif "LSHIFT" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_left(optiona, optionb, options[4], wires)
                used = True

        elif "RSHIFT" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_right(optiona, optionb, options[4], wires)
                used = True
        elif "NOT" in next_command:
            options = next_command.split(" ")
            optiona = options[1]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_not(optiona, options[3], wires)
                used = True
        else:
            options = next_command.split(" ")
            optiona = options[0]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.in_signal(options[0], options[2], wires)
                used = True

        if not used:
            commands.append(next_command)
    print(f'The end has completed with dict of {wires}')
    print(f'a has a value of {wires["a"]}')
    print("=============================================\n\n")


def test2():
    pass


def live2():
    print("=============================================")
    print("Starting live run 1")
    commands = helper.get_input("input2.txt")
    wires = {}

    while len(commands) > 0:
        next_command = commands.pop(0)
        used = False

        if "AND" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if (optiona.isdigit() or optiona in wires.keys()) and (optionb.isdigit() or optionb in wires.keys()):
                wires = helper.bit_and(optiona, optionb, options[4], wires)
                used = True

        elif "OR" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if (optiona.isdigit() or optiona in wires.keys()) and (optionb.isdigit() or optionb in wires.keys()):
                wires = helper.bit_or(optiona, optionb, options[4], wires)
                used = True

        elif "LSHIFT" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_left(optiona, optionb, options[4], wires)
                used = True

        elif "RSHIFT" in next_command:
            options = next_command.split(" ")
            optiona, optionb = options[0], options[2]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_right(optiona, optionb, options[4], wires)
                used = True
        elif "NOT" in next_command:
            options = next_command.split(" ")
            optiona = options[1]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.bit_not(optiona, options[3], wires)
                used = True
        else:
            options = next_command.split(" ")
            optiona = options[0]

            if optiona.isdigit() or optiona in wires.keys():
                wires = helper.in_signal(options[0], options[2], wires)
                used = True

        if not used:
            commands.append(next_command)
    print(f'The end has completed with dict of {wires}')
    print(f'a has a value of {wires["a"]}')
    print("=============================================\n\n")


test()
live()
# test2()
live2()

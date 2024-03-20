def get_input(filename):
    with open(filename) as file:
        temp = file.readlines()
    new_temp = []
    for i in temp:
        new_temp.append(i.strip())
    return new_temp


def get_code_length(code):
    return len(code)


def get_string_length(code):
    stripped = code[1:len(code)-1]
    string_length = 0
    string_list = []

    if len(stripped) > 0:
        for i in stripped:
            string_list.append(i)

        while len(string_list) > 0:
            next_char = string_list.pop(0)

            if next_char == "\\":
                if string_list[0] == "\\":
                    dump = string_list.pop(0)
                    string_length +=1
                elif string_list[0] == "\"":
                    dump = string_list.pop(0)
                    string_length += 1
                else:
                    hex_code = ''.join(string_list[1:3])
                    string_list = string_list[3:]
                    decoded = chr(int(hex_code, 16))
                    string_length += len(decoded)

            else:
                string_length += 1

    else:
        return 0

    return string_length


def get_string_length_recoded(code):
    stripped = code[1:len(code)-1]
    code_length = len(code) + 4
    string_list = []

    if len(stripped) > 0:
        for i in stripped:
            string_list.append(i)

        while len(string_list) > 0:
            next_char = string_list.pop(0)

            if next_char == "\\":
                if string_list[0] == "\\":
                    dump = string_list.pop(0)
                    code_length += 2
                elif string_list[0] == "\"":
                    dump = string_list.pop(0)
                    code_length += 2
                else:
                    string_list = string_list[3:]
                    code_length += 1

    return code_length

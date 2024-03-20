import codecs

import helper


def test():
    print("===================")
    print("Starting test run 1")
    code = helper.get_input("test_input.txt")
    code_length = 0
    string_length = 0
    for i in code:
        length = helper.get_code_length(i)
        code_length += length
        string_length += helper.get_string_length(i)

    print(f'The total length is {code_length}')
    print(f'The length of string is {string_length}')
    print(f'The length of code minus the string length is {code_length - string_length}')
    print("===================\n")


def live():
    print("===================")
    print("Starting live run 1")
    code = helper.get_input("input.txt")
    code_length = 0
    string_length = 0
    for i in code:
        length = helper.get_code_length(i)
        code_length += length
        string_length += helper.get_string_length(i)

    print(f'The total length is {code_length}')
    print(f'The length of string is {string_length}')
    print(f'The length of code minus the string length is {code_length - string_length}')
    print("===================\n")


def test2():
    print("===================")
    print("Starting test run 2")
    code = helper.get_input("test_input.txt")
    code_length = 0
    string_length = 0
    recoded_length = 0
    for i in code:
        length = helper.get_code_length(i)
        code_length += length
        string_length += helper.get_string_length(i)
        recoded_length += helper.get_string_length_recoded(i)

    print(f'The total length is {code_length}')
    print(f'The recoded length is {recoded_length}')
    print(f'The new length of string chars minus code length is {recoded_length - code_length}')
    print("===================\n")


def live2():
    print("===================")
    print("Starting live run 2")
    code = helper.get_input("input.txt")
    code_length = 0
    string_length = 0
    recoded_length = 0
    for i in code:
        length = helper.get_code_length(i)
        code_length += length
        string_length += helper.get_string_length(i)
        recoded_length += helper.get_string_length_recoded(i)

    print(f'The total length is {code_length}')
    print(f'The recoded length is {recoded_length}')
    print(f'The new length of string chars minus code length is {recoded_length - code_length}')
    print("===================")


test()
live()
test2()
live2()

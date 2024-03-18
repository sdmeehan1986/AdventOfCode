import hashlib


def get_input(file_name):
    with open(file_name) as file:
        return file.read()


def test():
    text = "abcdef"
    found = False
    hasher = hashlib.md5(text.encode('utf-8')).hexdigest()

    print(hasher[:5])
    if "00000" == hasher[:5]:
        found = True

    i = 0

    while not found:
        new_text = text + str(i)
        hasher = hashlib.md5(new_text.encode('utf-8')).hexdigest()
        if "00000" == hasher[:5]:
            found = True
            print(new_text)
        else:
            i += 1

    print("====================")


def live():
    text = "yzbqklnj"
    found = False
    hasher = hashlib.md5(text.encode('utf-8')).hexdigest()

    print(hasher[:5])
    if "00000" == hasher[:5]:
        found = True

    i = 0

    while not found:
        new_text = text + str(i)
        hasher = hashlib.md5(new_text.encode('utf-8')).hexdigest()
        if "00000" == hasher[:5]:
            found = True
            print(new_text)
        else:
            i += 1

    print("====================")


def test2():
    pass
    # No test2 for day 4


def live2():
    text = "yzbqklnj"
    found = False
    hasher = hashlib.md5(text.encode('utf-8')).hexdigest()

    print(hasher[:6])
    if "000000" == hasher[:6]:
        found = True
        print(text)

    i = 0

    while not found:
        new_text = text + str(i)
        hasher = hashlib.md5(new_text.encode('utf-8')).hexdigest()
        if "000000" == hasher[:6]:
            found = True
            print(new_text)
        else:
            i += 1

    print("====================")


test()
live()
# test2()
live2()

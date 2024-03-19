import numpy as np
import collections


def get_input(file_name):
    with open(file_name) as file:
        return file.readlines()


def builder():
    array = np.zeros((1000, 1000))
    return array


def toggle(start, end, array):
    start_co = start.split(",")
    end_co = end.split(",")

    start_co[0] = int(start_co[0])
    start_co[1] = int(start_co[1])
    end_co[0] = int(end_co[0])
    end_co[1] = int(end_co[1])

    for i in range(start_co[0], end_co[0]+1):
        for j in range(start_co[1], end_co[1]+1):
            if array[i][j] == 0:
                array[i][j] = 1
                # print(f'switching off {i},{j}')
            else:
                array[i][j] = 0
                # print(f'switching on {i},{j}')

    return array


def toggle_p2(start, end, array):
    start_co = start.split(",")
    end_co = end.split(",")

    start_co[0] = int(start_co[0])
    start_co[1] = int(start_co[1])
    end_co[0] = int(end_co[0])
    end_co[1] = int(end_co[1])

    for i in range(start_co[0], end_co[0]+1):
        for j in range(start_co[1], end_co[1]+1):
            array[i][j] = array[i][j] + 2

    return array


def on(start, end, array):
    start_co = start.split(",")
    end_co = end.split(",")

    start_co[0] = int(start_co[0])
    start_co[1] = int(start_co[1])
    end_co[0] = int(end_co[0])
    end_co[1] = int(end_co[1])

    for i in range(start_co[0], end_co[0]+1):
        for j in range(start_co[1], end_co[1]+1):
            array[i][j] = 1
            # print(f'switching on {i},{j}')

    return array


def on_p2(start, end, array):
    start_co = start.split(",")
    end_co = end.split(",")

    start_co[0] = int(start_co[0])
    start_co[1] = int(start_co[1])
    end_co[0] = int(end_co[0])
    end_co[1] = int(end_co[1])

    for i in range(start_co[0], end_co[0]+1):
        for j in range(start_co[1], end_co[1]+1):
            array[i][j] = array[i][j] + 1
            # print(f'switching on {i},{j}')

    return array


def off(start, end, array):
    start_co = start.split(",")
    end_co = end.split(",")

    start_co[0] = int(start_co[0])
    start_co[1] = int(start_co[1])
    end_co[0] = int(end_co[0])
    end_co[1] = int(end_co[1])

    for i in range(start_co[0], end_co[0]+1):
        for j in range(start_co[1], end_co[1]+1):
            array[i][j] = 0
            # print(f'switching off {i},{j}')

    return array


def off_p2(start, end, array):
    start_co = start.split(",")
    end_co = end.split(",")

    start_co[0] = int(start_co[0])
    start_co[1] = int(start_co[1])
    end_co[0] = int(end_co[0])
    end_co[1] = int(end_co[1])

    for i in range(start_co[0], end_co[0]+1):
        for j in range(start_co[1], end_co[1]+1):
            if array[i][j] > 0:
                array[i][j] = array[i][j] - 1
                # print(f'switching off {i},{j}')

    return array


def counter(array):
    on = (array == 1).sum()
    off = (array == 0).sum()

    return [off, on]


def counter_p2(array):
    brightness = 0

    for i in array:
        for j in i:
            if j > 0:
                brightness = brightness + j

    return brightness

import helper
from itertools import permutations


def test():
    print("===================")
    print("Starting test run 1")
    data = helper.get_input("test_input.txt")
    data_dict = helper.data_parser(data)

    print(data_dict)
    routes = permutations(data_dict)
    longest, shortest = helper.distances(data_dict, routes)
    print(f'Longest run is {longest}, and shortest run is {shortest}')
    print("===================\n")


def live():
    print("===================")
    print("Starting test run 1")
    data = helper.get_input("input.txt")
    data_dict = helper.data_parser(data)

    print(data_dict)
    routes = permutations(data_dict)
    longest, shortest = helper.distances(data_dict, routes)
    print(f'Longest run is {longest}, and shortest run is {shortest}')
    print("===================\n")


test()
live()

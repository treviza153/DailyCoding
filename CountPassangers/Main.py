#!/usr/local/bin python3


def count_passengers(list_num):

    return sum(on - off for on, off in list_num)


if __name__ == '__main__':

    list_numbers = [[10, 0], [3, 5], [5, 8]]

    print(count_passengers(list_numbers))

#!/usr/local/bin python3


def is_triangle(f1, f2, f3):

    return abs(f1 - f2) < f3 < f1 + f2


if __name__ == '__main__':
    l1 = 2
    l2 = 2
    l3 = 1

    print(is_triangle(l1, l2, l3))

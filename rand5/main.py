#!/usr/local/bin python3
import random


def rand5():
    """
    :return: integer from 1 to 5 with uniform probability
    """
    return random.randint(1, 5)


def rand7():
    """
    :return: integer from 1 to 7 with uniform probability
    """

    rand = 5*rand5() + rand5() - 5
    if rand < 22:
        return rand % 7 + 1
    return rand7()


if __name__ == '__main__':
    print("Random number from 1 to 7: ")
    print(rand7())

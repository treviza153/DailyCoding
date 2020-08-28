#!/usr/local/bin python3


def factivel(mgz, ran):
    result = filter(lambda x: ran.count(x) > mgz.count(x), ran)
    if result:
        return False
    return True


if __name__ == '__main__':
    magazine = "aabca"
    ransom = "aabca"

    print(factivel(magazine, ransom))

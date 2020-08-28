#!/usr/local/bin python3


def choose_winner(charlie, bob):
    res = [0, 0]
    for x in range(len(charlie)):
        if charlie[x] > bob[x]:
            res[0] += 1
        elif bob[x] > charlie[x]:
            res[1] += 1
    return res


if __name__ == '__main__':
    list_charlie = [8, 9, 3]
    list_bob = [5, 6, 3]

    result = choose_winner(list_charlie, list_bob)

    print(result)

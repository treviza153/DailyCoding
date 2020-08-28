#!/usr/local/bin python3


def countVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = filter(lambda x: x in vowels, word)
    return len(result)


if __name__ == '__main__':
    word = 'abracadabra'

    result = countVowels(word)
    print(result)

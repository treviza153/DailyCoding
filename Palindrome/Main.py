#!/usr/local/bin python3


def test_palindrome(frs):

    string = frs.upper().replace(" ", "")
    return 'Its a Palindrome' if string == string[::-1] else 'Its not a Palindrome'


if __name__ == '__main__':
    #string = 'apos a sopa'
    string = 'o lobo ama o bolo'

    print(test_palindrome(string))

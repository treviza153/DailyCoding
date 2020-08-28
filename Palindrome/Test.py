#!/usr/local/bin python3
import Main
import unittest


class Test(unittest.TestCase):

    def test_is_palindrome(self):
        string = 'Apos a Sopa'
        self.assertEqual(Main.test_palindrome(string), 'Its a Palindrome', 'Should be a Palindrome')

    def test_not_palindrome(self):
        string = 'O lobo ama a Torta'
        self.assertEqual(Main.test_palindrome(string), 'Its not a Palindrome', 'Should be a Palindrome')


if __name__ == '__main__':
    unittest.main()
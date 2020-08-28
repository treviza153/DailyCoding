#!/usr/local/bin python3
import Main
import unittest


class TestVowels(unittest.TestCase):

    def testCountVowels01(self):
        word = 'abracadabra' 
        self.assertEqual(Main.countVowels(word), 5, "Should be 5 vowels")

    def testCountVowels02(self):
        word = 'paraguai'
        self.assertEqual(Main.countVowels(word), 5, "Should be 4 vowels")


if __name__ == '__main__':
    unittest.main()

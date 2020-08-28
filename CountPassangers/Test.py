#!/usr/local/bin python3
import Main
import unittest


class TestList(unittest.TestCase):

    def testCountPass01(self):
        list_numbers = [[10, 0], [3, 5], [5, 8]]
        self.assertEqual(Main.count_passengers(list_numbers), 5, "Should be 5")

    def testCountPass02(self):
        list_numbers = [[10, 2], [3, 5], [5, 8]]
        self.assertEqual(Main.count_passengers(list_numbers), 3, "Should be 3")


if __name__ == '__main__':
    unittest.main()

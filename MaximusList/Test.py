#!/usr/local/bin python3
import Main
import unittest


class TestMaxList(unittest.TestCase):

    def testMaxList01(self):
        num = 4
        array = [10, 5, 2, 7, 8, 7]
        self.assertEqual(Main.maxList(num, array), [10, 8, 8],
                         "Should be [10, 8, 8]")

    def testMaxList02(self):
        num = 3
        array = [10, 5, 2, 7, 8, 7]
        self.assertEqual(Main.maxList(num, array), [10, 7, 8, 8],
                         "Should be [10, 7, 8, 8]")


if __name__ == '__main__':
    unittest.main()

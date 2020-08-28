#!/usr/local/bin python3
import Main
import unittest


class TestList(unittest.TestCase):

    def testNumDivisible10(self):
        self.assertEqual(Main.numDivisible(10), [2,5], "Should be [2,5]")
        
    def testNumDivisible30(self):
        self.assertEqual(Main.numDivisible(30), [2, 3, 5, 6, 10, 15], "Should be [2, 3, 5, 6, 10, 15]")


if __name__ == '__main__':
    unittest.main()
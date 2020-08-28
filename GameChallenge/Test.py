#!/usr/local/bin python3
import Main
import unittest


class TestChallenge(unittest.TestCase):

    def testCharlieWin(self):
        Charlie = [7,8,10,3]
        Bob = [6,5,10,4]
        self.assertEqual(Main.chooseWinner(Charlie,Bob), [2,1], "Should be [2,1]")

    def testBobWin(self):
        Charlie = [4,5,9]
        Bob = [6,10,12]
        self.assertEqual(Main.chooseWinner(Charlie,Bob), [0,3], "Should be [0,3]")


if __name__ == '__main__':
    unittest.main()

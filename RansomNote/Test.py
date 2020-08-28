#!usr/local/bin python3
import Main
import unittest

class TesTList(unittest.TestCase):

    def testFactivel01(self):
        mgz = "aabca"
        ran = "aaaab"
        self.assertEqual(Main.factivel(mgz, ran), False, "Should be False")

    # def testFactivel02(self):
    #     mgz = "aabca"
    #     ran = "aabca"
    #     self.assertEqual(Main.factivel(mgz, ran), True, "Should be True")


if __name__ == "__main__":
    unittest.main()
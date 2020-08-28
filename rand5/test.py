#!/usr/local/bin python3
import main
import unittest


class Test(unittest.TestCase):

    def test_return_integer(self):
        """
        Check if the rand7 returns an integer from 1 to 7.
        """
        for _ in range(10000):
            number = main.rand7()
            if not 0 < number < 8:
                self.assertFalse("The integer is not from 1 to 7.")
        self.assertTrue("The integer is always from 1 to 7.")

    def test_uniform_probability(self):
        """
        Checks if the probability is uniform.
        """
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        total = 10000
        percent = float(1)/float(7)*100
        for _ in range(total):
            number = main.rand7()
            if number == 1:
                count1 += 1
            elif number == 2:
                count2 += 1
            elif number == 3:
                count3 += 1
            elif number == 4:
                count4 += 1
            elif number == 5:
                count5 += 1
            elif number == 6:
                count6 += 1
            elif number == 7:
                count7 += 1
        counts = list((float(count1)/float(total)*100,
                       float(count2)/float(total)*100,
                       float(count3)/float(total)*100,
                       float(count4)/float(total)*100,
                       float(count5)/float(total)*100,
                       float(count6)/float(total)*100,
                       float(count7)/float(total)*100))
        for count in counts:
            if not percent - 1 < count < percent + 1:
                self.assertFalse("The probability is not uniform.")
        self.assertTrue("The probability is uniform.")


if __name__ == '__main__':
    unittest.main()

import unittest
from solutions.day_1_1 import *
from solutions.day_1_2 import *
from solutions.day_2_1 import *
from solutions.day_2_2 import *
from solutions.day_4_1 import *
from solutions.day_4_2 import *
from solutions.day_5_1_2 import *
from solutions.day_6_1 import *
from solutions.day_7_1 import *
from solutions.day_8_1 import *


class TestSolutions(unittest.TestCase):

    def test_day_1_1(self):
        self.assertEqual(day_1_1(), 69883, "Expected 69883")

    # def test_day_1_2(self):
    #     self.assertEqual(day_1_2(), 207576, "Excepted 207576")

    def test_day_2_1(self):
        self.assertEqual(day_2_1(), 12156, "Expected 12156")

    def test_day_2_2(self):
        self.assertEqual(day_2_2(), 10835, "Expected 10835")

    def test_day_4_1(self):
        self.assertEqual(day_4_1(), 477, "Expected 477")

    def test_day_4_2(self):
        self.assertEqual(day_4_2(), 830, "Expected 830")

    def test_day_5_1(self):
        self.assertEqual(day_5_1_2(1), "VJSFHWGFT", "Expected VJSFHWGFT")
        self.assertEqual(day_5_1_2(2), "LCTQFBVZV", "Expected LCTQFBVZV")

    def test_day_6_1(self):
        self.assertEqual(day_6_1(), 69, "Expect 69")

    # def test_day_7_1(self):
    #     self.assertEqual(day_7_1(), 69, "Expect 69")

    def test_day_8_1(self):
        self.assertEqual(day_8_1(1), 1703, "Expected 1703")
        self.assertEqual(day_8_1(2), 496650, "Expected 496650")


if __name__ == '__main__':
    unittest.main()

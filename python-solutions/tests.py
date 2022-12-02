import unittest
from solutions.day_1_1 import *
from solutions.day_1_2 import *
from solutions.day_2_1 import *
from solutions.day_2_2 import *


class TestSolutions(unittest.TestCase):

    def test_day_1_1(self):
        self.assertEqual(day_1_1(), 69883, "Expected 69883")

    # def test_day_1_2(self):
    #     self.assertEqual(day_1_2(), 207576, "Excepted 207576")

    def test_day_2_1(self):
        self.assertEqual(day_2_1(), 12156, "Expected 12156")

    def test_day_2_2(self):
        self.assertEqual(day_2_2(), 10835, "Expected 10835")


if __name__ == '__main__':
    unittest.main()

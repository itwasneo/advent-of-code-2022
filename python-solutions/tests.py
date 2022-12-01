import unittest
from solutions.day_1_1 import *


class TestSolutions(unittest.TestCase):

    def test_day_1_1(self):
        self.assertEqual(day_1_1(), 774967, "Expected 774967")


if __name__ == '__main__':
    unittest.main()

import unittest
from group_task17 import num_ways


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(num_ways(6, [1, 5]), 2)

    def test_case_2(self):
        self.assertEqual(num_ways(25, [1, 5, 10, 25]), 13)

    def test_case_3(self):
        self.assertEqual(num_ways(12, [2, 3, 7]), 4)

    def test_case_4(self):
        self.assertEqual(num_ways(0, [2, 3, 4, 7]), 1)

    def test_case_5(self):
        self.assertEqual(num_ways(9, [5]), 0)

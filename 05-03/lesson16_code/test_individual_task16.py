import unittest
from .individual_task3 import move_num_to_end


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        target = 2
        expected_start = [1, 3, 4]
        expected_end = [2, 2, 2, 2, 2]
        output = move_num_to_end(array, target)
        output_start = sorted(output[0:3])
        output_end = output[3:]
        self.assertEqual(output_start, expected_start)
        self.assertEqual(output_end, expected_end)

    def test_case_2(self):
        array = []
        target = 3
        expected = []
        output = move_num_to_end(array, target)
        self.assertEqual(output, expected)

    def test_case_3(self):
        array = [1, 2, 4, 5, 6]
        target = 3
        expected = [1, 2, 4, 5, 6]
        output = move_num_to_end(array, target)
        self.assertEqual(output, expected)

    def test_case_4(self):
        array = [3, 3, 3, 3, 3]
        target = 3
        expected = [3, 3, 3, 3, 3]
        output = move_num_to_end(array, target)
        self.assertEqual(output, expected)

    def test_case_5(self):
        array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        target = 5
        expected_start = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        expected_end = [5, 5, 5, 5, 5, 5]
        output = move_num_to_end(array, target)
        output_start = sorted(output[0:11])
        output_end = output[11:]
        self.assertEqual(output_start, expected_start)
        self.assertEqual(output_end, expected_end)

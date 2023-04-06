import unittest
from individual_task17 import group_anagrams


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [["yo", "oy"], ["flop", "olfp"],
                    ["act", "tac", "cat"], ["foo"]]
        output = list(map(lambda x: sorted(x), group_anagrams(words)))
        self.compare(expected, output)

    def test_case_2(self):
        words = []
        expected = []
        output = group_anagrams(words)
        self.compare(expected, output)

    def test_case_3(self):
        words = ["test"]
        expected = [["test"]]
        output = group_anagrams(words)
        print(output)
        self.compare(expected, output)

    def test_case_4(self):
        words = ["abc", "cba", "bca"]
        expected = [["abc", "cba", "bca"]]
        output = list(map(lambda x: sorted(x), group_anagrams(words)))
        print(output)
        self.compare(expected, output)

    def test_case_5(self):
        words = ["cinema", "a", "flop", "iceman", "meacyne", "lofp", "olfp"]
        expected = [
            ["a"],
            ["meacyne"],
            ["cinema", "iceman"],
            ["flop", "lofp", "olfp"]
        ]
        output = list(map(lambda x: sorted(x), group_anagrams(words)))
        print(output)
        self.compare(expected, output)

    def compare(self, expected, output):
        if len(expected) == 0:
            self.assertEqual(output, expected)
            return
        self.assertEqual(len(expected), len(output))
        for group in expected:
            self.assertTrue(sorted(group) in output)

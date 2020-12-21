
import unittest
from easy.single_row_keyboard.src.solution import Solution


class MyTestCase(unittest.TestCase):

    def test_shorter_statement(self):
        solution = Solution()
        expected = 4
        actual = solution.calculate_time("abcdefghijklmnopqrstuvwxyz", "cba")
        self.assertEqual(expected, actual)

    def test_longer_statement(self):
        solution = Solution()
        expected = 73
        actual = solution.calculate_time("pqrstuvwxyzabcdefghijklmno", "leetcode")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

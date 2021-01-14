import unittest
from easy.shuffle_the_array.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_shuffle_odd_length(self):
        expected = [2, 3, 5, 4, 1, 7]
        solution = Solution()
        actual = solution.shuffle([2, 5, 1, 3, 4, 7], 3)
        self.assertEqual(expected, actual)

    def test_shuffle_even_length(self):
        expected = [1, 4, 2, 3, 3, 2, 4, 1]
        solution = Solution()
        actual = solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

import unittest
from easy.get_max_elem_from_generated_array.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_length_seven(self):
        solution = Solution()
        expected = 3
        actual = solution.getMaximumGenerated(7)
        self.assertEqual(expected, actual)

    def test_length_two(self):
        solution = Solution()
        expected = 1
        actual = solution.getMaximumGenerated(2)
        self.assertEqual(expected, actual)

    def test_length_three(self):
        solution = Solution()
        expected = 2
        actual = solution.getMaximumGenerated(3)
        self.assertEqual(expected, actual)

    def test_length_three(self):
        solution = Solution()
        expected = 0
        actual = solution.getMaximumGenerated(0)
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()

import unittest

from medium.string_to_integer.src.solution import Solution


class MyTestCase(unittest.TestCase):

    def test_normal_numeric(self):
        solution = Solution()
        expected = 42
        actual = solution.myAtoi("42")

        self.assertEqual(expected, actual)

    def test_prefix_white_space(self):
        solution = Solution()
        expected = -42
        actual = solution.myAtoi("   -42")

        self.assertEqual(expected, actual)

    def test_suffix_non_digits(self):
        solution = Solution()
        expected = 4193
        actual = solution.myAtoi("4193 with words")

        self.assertEqual(expected, actual)

    def test_prefix_non_digits(self):
        solution = Solution()
        expected = 0
        actual = solution.myAtoi("words and 987")

        self.assertEqual(expected, actual)

    def test_normal_decimal(self):
        solution = Solution()
        expected = 3
        actual = solution.myAtoi("3.14159")
        self.assertEqual(expected, actual)


    def test_composite(self):
        solution = Solution()
        expected = 0
        actual = solution.myAtoi("+-12")
        self.assertEqual(expected, actual)


    def test_white_space(self):
        solution = Solution()
        expected = 0
        actual = solution.myAtoi("")

        self.assertEqual(expected, actual)

    def test_plus_only(self):
        solution = Solution()
        expected = 0
        actual = solution.myAtoi("+")

    def test_composite_numeric(self):
        solution = Solution()
        expected = 0
        actual = solution.myAtoi("00000-42a1234")

        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()

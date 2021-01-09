import unittest
from easy.valid_palindrome_2.src.solution import Solution


class MyTestCase(unittest.TestCase):
    solution = Solution()

    def test_valid_standard_palindrome(self):
        expected = True
        solution = Solution()

        actual = solution.validPalindrome("aba")

        self.assertEqual(expected, actual)

    def test_valid_could_delete_palindrome(self):
        expected = True
        solution = Solution()

        actual = solution.validPalindrome("abca")

        self.assertEqual(expected, actual)

    def test_invalid_palindrome(self):
        expected = False
        solution = Solution()

        actual = solution.validPalindrome("abc")

        self.assertEqual(expected, actual)

    def test_valid_palindrome_more_string(self):
        expected = True
        solution = Solution()

        actual = solution.validPalindrome("eccer")

        self.assertEqual(expected, actual)

    def test_invalid_palindrome_more_string(self):
        expected = False
        solution = Solution()
        actual = solution.validPalindrome("atbbga")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

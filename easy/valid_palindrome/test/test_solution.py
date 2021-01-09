import unittest
from easy.valid_palindrome.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_kamma_coron(self):
        solution = Solution()
        expected = True
        actual = solution.isPalindrome("A man, a plan, a canal: Panama")

        self.assertEqual(expected, actual)

    def test_white_space(self):
        solution = Solution()
        expected = False
        actual = solution.isPalindrome("race a car")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

import unittest

from easy.check_if_a_number_is_majority_elem.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something_one(self):
        solution = Solution()
        expected = True
        actual = solution.isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5)
        self.assertEqual(expected, actual)

    def test_something_second(self):
        solution = Solution()
        expected = False
        actual = solution.isMajorityElement([10, 100, 101, 101], 101)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

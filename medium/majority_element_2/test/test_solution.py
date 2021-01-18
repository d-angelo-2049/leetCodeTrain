import unittest
from medium.majority_element_2.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_three_length_array(self):
        solution = Solution()
        expected = [3]
        actual = solution.majorityElement([3, 2, 3])
        self.assertEqual(expected, actual)

    def test_one_length_array(self):
        solution = Solution()
        expected = [1]
        actual = solution.majorityElement([1])

        self.assertEqual(expected, actual)

    def test_two_length_array(self):
        solution = Solution()
        expected = [1, 2]
        actual = solution.majorityElement([1,2])

        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()

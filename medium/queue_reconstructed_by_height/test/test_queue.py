import unittest

from medium.queue_reconstructed_by_height.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        actual = solution.reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
        self.assertEqual(actual, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()

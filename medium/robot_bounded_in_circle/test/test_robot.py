import unittest
from medium.robot_bounded_in_circle.src.solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something_1(self):
        solution = Solution()
        instructions = "GGLLGG"
        expected = True

        actual = solution.isRobotBounded(instructions)
        self.assertEqual(expected, actual)

    def test_something_2(self):
        solution = Solution()
        instructions = "GG"
        expected = False

        actual = solution.isRobotBounded(instructions)
        self.assertEqual(expected, actual)

    def test_something_3(self):
        solution = Solution()
        instructions = "GL"
        expected = True

        actual = solution.isRobotBounded(instructions)
        self.assertEqual(expected, actual)

    def test_something_4(self):
        solution = Solution()
        instructions = "GLGLGGLGL"
        expected = False

        actual = solution.isRobotBounded(instructions)
        self.assertEqual(expected, actual)

    def test_something_5(self):
        solution = Solution()
        instructions = "GLRLLGLL"
        expected = True

        actual = solution.isRobotBounded(instructions)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

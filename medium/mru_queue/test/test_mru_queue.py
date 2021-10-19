import unittest
from medium.mru_queue.src.mru_queue import MruQueue


class MyTestCase(unittest.TestCase):
    def test_something(self):

        queue = MruQueue(8)
        actual1 = queue.fetch(3)

        self.assertEqual(actual1, 3)

        actual2 = queue.fetch(5)
        self.assertEqual(actual2, 6)

        actual3 = queue.fetch(2)
        self.assertEqual(actual3, 2)

        actual4 = queue.fetch(8)
        self.assertEqual(actual4, 2)


if __name__ == '__main__':
    unittest.main()

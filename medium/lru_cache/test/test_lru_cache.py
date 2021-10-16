import unittest
from medium.lru_cache.src.lru_cache import LruCache


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        cache = LruCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        actual1 = cache.get(1)
        self.assertEqual(actual1, 1)

        cache.put(3, 3)
        actual2 = cache.get(2)
        self.assertEqual(actual2, -1)

        cache.put(4, 4)
        actual3 = cache.get(1)
        self.assertEqual(actual3, -1)

        actual4 = cache.get(3)
        self.assertEqual(actual4, 3)

        actual5 = cache.get(4)
        self.assertEqual(actual5, 4)

    def test_case_2(self):
        cache = LruCache(2)
        actual1 = cache.get(2)
        self.assertEqual(actual1, -1)

        cache.put(2, 6)
        actual2 = cache.get(1)
        self.assertEqual(actual2, -1)

        cache.put(1, 5)
        cache.put(1, 2)
        actual3 = cache.get(1)
        self.assertEqual(actual3, 2)

        actual4 = cache.get(2)
        self.assertEqual(actual4, 6)


if __name__ == '__main__':
    unittest.main()

import unittest
from easy.palindrome_linked_list.src.solution import Solution
from easy.palindrome_linked_list.src.list_node import ListNode


class MyTestCase(unittest.TestCase):
    def test_palindrome_low_string(self):
        solution = Solution()

        node = ListNode(1, ListNode(2))
        actual = solution.isPalindrome(node)

        self.assertEqual(False, actual)

    def test_palindrome_more_string(self):

        solution = Solution()

        node = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        actual = solution.isPalindrome(node)

        self.assertEqual(True, actual)

    def test_palindrome_negative_string(self):

        solution = Solution()

        node = ListNode(-129, ListNode(-129))
        actual = solution.isPalindrome(node)

        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()

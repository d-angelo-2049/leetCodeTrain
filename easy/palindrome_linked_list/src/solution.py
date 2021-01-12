
from easy.palindrome_linked_list.src.list_node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        validation_src = []

        runner = head
        while runner is not None:
            validation_src.append(runner.val)
            runner = runner.next

        return validation_src == validation_src[::-1]


import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        target_str = pattern.sub('', s).lower()

        validation_length = len(target_str) // 2

        for i in range(validation_length):
            if target_str[i] != target_str[-1 - i]:
                return False
        return True

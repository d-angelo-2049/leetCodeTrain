class Solution:
    def validPalindrome(self, s: str) -> bool:
        # for i in range(len(s)):
        #     target = s[:i] + s[i + 1:]
        #     aaa = target[::-1]
        #     if target == aaa:
        #         return True
        # return s == s[::-1]
        return self.valid_palindrome_by_greedy(s)

    def valid_palindrome_by_greedy(self, s: str) -> bool:
        def is_pali_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
        return True

    def my_valid_palindrome(self, s: str) -> bool:
        length = len(s)
        validation_length = len(s) // 2
        is_continuously = False

        for i in range(validation_length):
            if s[i] != s[-1 - i]:
                is_continuously = True
        if not is_continuously:
            return True

        is_palindrome = True
        for target_index in range(length):
            is_palindrome = True
            target_str = self._targetStr(s, target_index)
            for i in range(len(target_str) // 2):
                if target_str[i] != target_str[-1 - i]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return is_palindrome
        return is_palindrome

    def _targetStr(self, s: str, target: int) -> str:
        if target != -1:
            return s[:target] + s[target + 1:]
        return s

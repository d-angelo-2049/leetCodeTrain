
class Solution(object):

    def calculate_time(self, keyboard: str, word: str) -> int:

        finger_index = 0
        diff = 0
        for c in word:
            match_index = keyboard.find(c)
            if match_index != -1:
                diff += abs(match_index - finger_index)
                finger_index = match_index

        return diff

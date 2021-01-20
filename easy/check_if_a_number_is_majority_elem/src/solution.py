import collections


class Solution:

    def isMajorityElement(self, nums, target: int) -> bool:
        counter = collections.Counter(nums)

        if counter[target] > len(nums) // 2:
            return True

        for k, v in counter.items():
            if counter[target] <= v:
                return False

        return True

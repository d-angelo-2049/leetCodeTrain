class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        max_key = 0
        for k, v in counter.items():
            if v > len(nums) // 2:
                return k
            if v > counter[max_key]:
                max_key = k
        return counter[max_key]

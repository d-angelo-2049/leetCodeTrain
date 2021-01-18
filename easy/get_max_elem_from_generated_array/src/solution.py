class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if 0 == n:
            return 0

        length = n + 1
        nums = [0] * length

        nums[1] = 1
        maximum = nums[1]

        for i in range(length):
            if i % 2 == 0:
                k = i // 2
                nums[2 * k] = nums[k]
                maximum = self.greater_number(maximum, nums[2 * k])

            elif i % 2 == 1:
                k = (i - 1) // 2
                nums[2 * k + 1] = nums[k] + nums[k + 1]
                maximum = self.greater_number(maximum, nums[2 * k + 1])
        return maximum

    def greater_number(self, first, second):
        if first > second:
            return first
        else:
            return second

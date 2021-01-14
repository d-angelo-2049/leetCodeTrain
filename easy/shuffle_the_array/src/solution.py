class Solution:

    def shuffle(self, nums, m: int) -> []:
        shuffle_list = []
        for index in range(m):
            shuffle_list.extend([nums[index], nums[index + m]])
        return shuffle_list

    def my_shuffle(self, nums, m: int) -> []:
        shuffle_list = []
        for index in range(m):
            shuffle_list.append(nums[index])
            shuffle_list.append(nums[m + index])
        return shuffle_list

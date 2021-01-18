import collections


class Solution():
    def my_majorityElement(self, nums) -> []:

        standard_counts = len(nums)
        majority_dict = {}
        majority_list = []

        for elem in nums:
            counter = majority_dict.get(elem, 0)
            counter = counter + 1
            majority_dict.update({elem: counter})

        for k, v in majority_dict.items():
            if v > (standard_counts / 3):
                majority_list.append(k)

        return majority_list

    def majorityElement(self, nums) -> []:

        counter = collections.Counter(nums)
        majority_list = []
        for k, v in counter.items():
            if v > (len(nums) / 3):
                majority_list.append(k)
        return majority_list

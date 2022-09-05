from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_sum and dict_sum[complement] != i:
                return [i, dict_sum[complement]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_sum and dict_sum[complement] != i:
                return [i, dict_sum[complement]]


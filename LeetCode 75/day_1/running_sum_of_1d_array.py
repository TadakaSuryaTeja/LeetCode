from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_sum = 0
        result_list = []
        for i in nums:
            result_sum += i
            result_list.append(result_sum)
        return result_list

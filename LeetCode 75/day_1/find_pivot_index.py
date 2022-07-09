from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = sum(nums)
        right = 0
        for i in range(len(nums)):
            left -= nums[i]
            if right == left:
                return i
            right += nums[i]
        return -1

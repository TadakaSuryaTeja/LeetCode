from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        len_n = len(nums)
        nums.sort()
        max_area = 0
        for i in range(len_n - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a + b > c and b + c > a and c + a > b:
                max_area = max(a + b + c, max_area)

        return max_area

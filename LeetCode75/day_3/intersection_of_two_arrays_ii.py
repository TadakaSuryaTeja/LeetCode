from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_nums = len(nums2)
        largest_num = nums2
        smallest_num = nums1
        if len(nums1) > len(nums2):
            len_nums = len(nums1)
            largest_num = nums1
            smallest_num = nums2

        result = []
        for i in range(len_nums):
            if largest_num[i] in smallest_num:
                result.append(largest_num[i])
                smallest_num.remove(largest_num[i])

        return result


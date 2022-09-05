import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]] + [0] * (len(nums) - 1)
        maxSum = sums[0]

        for i in range(1, len(nums)):
            sums[i] = max(nums[i], sums[i - 1] + nums[i])
            maxSum = max(maxSum, sums[i])

        return maxSum


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)]
    s = Solution()
    testable_functions = [s.maxSubArray]

    def test_max_subarray(self):
        for methods in self.testable_functions:
            for args, expected in self.test_cases:
                actual = methods(args)
                assert actual == expected, f"Failed {methods.__name__} for: {[args]}"


if __name__ == "__main__":
    unittest.main()

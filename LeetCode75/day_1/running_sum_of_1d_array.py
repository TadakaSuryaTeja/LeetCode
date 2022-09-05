import unittest
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [([1, 2, 3, 4], [1, 3, 6, 10])]
    s = Solution()
    testable_functions = [s.runningSum]

    def test_running_sum_array(self):
        for methods in self.testable_functions:
            for args, expected in self.test_cases:
                actual = methods(args)
                assert actual == expected, f"Failed {methods.__name__} for: {[args]}"


if __name__ == "__main__":
    unittest.main()

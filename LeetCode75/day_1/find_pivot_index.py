import unittest
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left_sum = 0
        for index, value in enumerate(nums):
            if left_sum == (s - left_sum - value):
                return index
            left_sum += value

        return -1


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [([1, 7, 3, 6, 5, 6], 3)]
    s = Solution()
    testable_functions = [s.pivotIndex]

    def test_find_pivot_index(self):
        for methods in self.testable_functions:
            for args, expected in self.test_cases:
                actual = methods(args)
                assert actual == expected, f"Failed {methods.__name__} for: {[args]}"


if __name__ == "__main__":
    unittest.main()

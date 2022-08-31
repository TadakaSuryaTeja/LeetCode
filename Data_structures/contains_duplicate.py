import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [([1, 2, 3, 1], True)]
    s = Solution()
    testable_functions = [s.containsDuplicate]

    def test_contains_duplicate(self):
        for methods in self.testable_functions:
            for args, expected in self.test_cases:
                actual = methods(args)
                assert actual == expected, f"Failed {methods.__name__} for: {[args]}"


if __name__ == "__main__":
    unittest.main()

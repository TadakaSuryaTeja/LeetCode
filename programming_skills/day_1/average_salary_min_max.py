from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        result = 0
        for i in salary:
            if i == min(salary) or i == max(salary):
                continue
            else:
                result +=i
        return result / (len(salary) - 2)

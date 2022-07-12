from functools import cache
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_matchsticks = sum(matchsticks)
        if sum_matchsticks < 4:
            return False
        if sum_matchsticks % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        edge = sum_matchsticks // 4

        @cache
        def calculate_match(l1, l2, l3, l4, i):
            nonlocal edge
            if l1 == l2 == l3 == l4 == edge:
                return True
            if i > len(matchsticks) - 1:
                return False
            if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
                return False
            return calculate_match(l1 + matchsticks[i], l2, l3, l4, i + 1) or \
                   calculate_match(l1, l2 + matchsticks[i], l3, l4, i + 1) or \
                   calculate_match(l1, l2, l3 + matchsticks[i], l4, i + 1) or \
                   calculate_match(l1, l2, l3, l4 + matchsticks[i], i + 1)

        return calculate_match(0, 0, 0, 0, 0)


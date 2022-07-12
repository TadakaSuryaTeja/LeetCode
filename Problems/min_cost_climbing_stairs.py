from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        global val_2
        if len(cost) == 0:
            return 0
        val_1 = cost[0]
        if len(cost) >= 2:
            val_2 = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(val_1, val_2)
            val_1 = val_2
            val_2 = cur

        return min(val_1, val_2)

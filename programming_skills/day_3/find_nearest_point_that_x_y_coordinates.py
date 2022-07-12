from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = 0
        idx = -1
        for index, value in enumerate(points):
            if value[0] == x or value[1] == y:
                current_distance = abs(x - value[0]) + abs(y - value[1])
                if current_distance < min_distance or idx == -1:
                    min_distance = current_distance
                    idx = index

        return idx

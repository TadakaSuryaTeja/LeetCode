class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 !=0 and high % 2 != 0:
            count = ((high-low+1)//2) + 1
        else:
            count = ((high-low+1)//2)
        return count

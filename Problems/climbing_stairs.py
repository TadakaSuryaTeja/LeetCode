class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2:
            return 2
        else:
            first = 1;
            second = 2;
            for i in range(2, n):
                third = first + second
                first = second
                second = third
            return second

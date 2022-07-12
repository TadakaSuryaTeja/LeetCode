class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_n = 0
        while n != 0:
            quotient = n%10
            sum_n += quotient
            product *= quotient
            n = n//10
        return product-sum_n

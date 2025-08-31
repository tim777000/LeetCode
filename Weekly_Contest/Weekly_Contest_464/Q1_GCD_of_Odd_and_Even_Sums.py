from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        odd_start = 1
        sumEven = 0
        even_start = 2
        for i in range(n):
            sumOdd += odd_start
            odd_start += 2
            sumEven += even_start
            even_start += 2
        return gcd(sumOdd, sumEven)

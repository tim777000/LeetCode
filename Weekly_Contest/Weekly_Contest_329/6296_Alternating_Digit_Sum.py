class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        sign = 1
        while (n > 0):
            answer += sign*(n%10)
            n = n//10
            sign = (-1)*sign
        return answer if sign == -1 else (-1)*answer
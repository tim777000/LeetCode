from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        half = k // 2
        first_k = 0
        first_k_modify = 0
        for i in range(k):
            first_k += prices[i] * strategy[i]
            first_k_modify += prices[i] * (0 if i < half else 1)
        precalculate = dict()
        for i in range(len(prices)-k+1):
            if (i == 0):
                precalculate[i] = (first_k, first_k_modify)
            else:
                first = prices[i-1] * strategy[i-1]
                mid = prices[i+half-1]
                last = prices[i+k-1] * strategy[i+k-1]
                last_modify = prices[i+k-1]
                precalculate[i] = (precalculate[i-1][0]-first+last, precalculate[i-1][1]-mid+last_modify)
        origin_result = 0
        for i in range(len(prices)):
            origin_result += prices[i] * strategy[i]
        result = origin_result
        for i in range(len(prices)-k+1):
            modify_result = origin_result
            modify_result -= precalculate[i][0]
            modify_result += precalculate[i][1]
            result = result if result > modify_result else modify_result
        return result

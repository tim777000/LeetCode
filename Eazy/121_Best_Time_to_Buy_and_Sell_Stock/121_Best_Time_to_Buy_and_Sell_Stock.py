from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_size = len(prices)
        max_profit = 0
        cumulate_profit = 0
        second_pointer = 0
        for i in range(prices_size):
            if (second_pointer == i):
                continue
            cumulate_profit += prices[i] - prices[i-1]
            if (cumulate_profit <= 0):
                cumulate_profit = 0
                second_pointer = i
                continue
            max_profit = max(cumulate_profit, max_profit)
        return max_profit

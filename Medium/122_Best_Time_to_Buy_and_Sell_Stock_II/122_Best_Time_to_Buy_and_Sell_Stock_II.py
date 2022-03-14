class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length_of_prices = len(prices)
        answer = 0
        max_price = 0
        for i in range(length_of_prices, 0, -1):
            if (prices[i-1] < max_price):
                answer += max_price - prices[i-1]
            max_price = prices[i-1]
        return answer

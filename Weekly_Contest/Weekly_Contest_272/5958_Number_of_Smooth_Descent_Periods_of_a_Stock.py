class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        compression_prices_list = []
        start_index, end_index = 0, 0
        pre_price = prices[0]
        for index, price in enumerate(prices):
            if (index == 0):
                continue
            elif (price + 1 == pre_price):
                pre_price = price
                end_index = index
            else:
                compression_prices_list.append((start_index, end_index))
                start_index, end_index = index, index
                pre_price = price
        compression_prices_list.append((start_index, end_index))

        answer = len(prices)
        for compression in compression_prices_list:
            answer += self.sigma_sum(compression[1] - compression[0])
        return answer

    def sigma_sum(self, target: int) -> int:
        answer = 0
        for i in range(0, target+1):
            answer += i
        return answer
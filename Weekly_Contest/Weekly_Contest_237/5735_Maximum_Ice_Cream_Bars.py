class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        answer = 0
        costs = sorted(costs)
        for i in costs:
            if coins >= i:
                coins -= i
                answer += 1
            else:
                break
        return answer

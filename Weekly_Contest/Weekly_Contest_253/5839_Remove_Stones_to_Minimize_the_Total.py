class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        negativePiles = [i*(-1) for i in piles]
        heapq.heapify(negativePiles)
        for i in range(0, k):
            temp = heapq.heappop(negativePiles)*(-1)
            temp -= floor(temp / 2)
            heapq.heappush(negativePiles, temp*(-1))
        return sum(negativePiles)*(-1)
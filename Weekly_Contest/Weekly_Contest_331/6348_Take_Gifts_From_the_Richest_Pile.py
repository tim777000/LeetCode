class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        neg_gifts = [ (-1)*gift for gift in gifts ]
        # O(n)
        heapq.heapify(neg_gifts)
        for i in range(0, k):
            # O(logn)
            richest = (-1)*heapq.heappop(neg_gifts)
            left_richest = isqrt(richest)
            # O(logn)
            heapq.heappush(neg_gifts, (-1)*left_richest)

        return (-1)*sum(neg_gifts)

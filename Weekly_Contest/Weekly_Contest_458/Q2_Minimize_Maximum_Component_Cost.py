class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        total_cut = len(edges) - (n-k)
        return sorted(edges, reverse=True, key=lambda x: x[2])[total_cut][2] if total_cut < len(edges) else 0

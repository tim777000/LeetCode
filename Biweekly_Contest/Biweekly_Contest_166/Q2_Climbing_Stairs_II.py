class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0]*(n+1)
        i = 1
        dp[i] = costs[i-1] + 1
        if n == i:
            return dp[i]
        i = 2
        dp[i] = min(dp[i-1] + costs[i-1] + 1, costs[i-1] + 4) 
        for i in range(3, n+1):
            dp[i] = min(dp[i-1] + costs[i-1] + 1, dp[i-2] + costs[i-1] + 4, dp[i-3] + costs[i-1] + 3**2)
        return dp[n]

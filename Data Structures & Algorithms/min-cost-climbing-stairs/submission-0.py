class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * (n+1)

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n+1):
            c = cost[i] if i < n else 0
            dp[i] = c + min(dp[i-1], dp[i-2])
        
        return dp[n]

        
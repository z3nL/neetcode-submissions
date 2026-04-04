class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Max money when house i is reached
        dp = [0]*n 
        dp[0] = nums[0]
        
        for i in range(1, n):
            # Previous house was robbed
            dont = dp[i-1]

            # Rob this one
            before = dp[i-2] if i > 1 else 0
            do = nums[i] + before

            dp[i] = max(dont, do)
        
        return dp[-1] 

        
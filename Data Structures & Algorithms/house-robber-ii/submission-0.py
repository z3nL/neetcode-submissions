class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] if nums else 0

        def rob2(houses):
            n = len(houses) 
            dp = [0] * len(houses)
            # Max money attainable by the time you reach house i
            for i in range(n):
                do = houses[i] + (dp[i-2] if i >= 2 else 0)
                dont = dp[i-1] if i >= 1 else 0
                dp[i] = max(do, dont)
            
            return dp[n-1]
        
        # Exclude either the first house or last house
        return max(rob2(nums[1:]), rob2(nums[:-1]))
            

            
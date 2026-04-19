class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # The length of the LIS in nums[:i]
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
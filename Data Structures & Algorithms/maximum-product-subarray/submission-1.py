class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')

        # Track current lowest/highest product
        lo, hi = 1, 1

        for n in nums:
            # A subarray containing 0 is automatically zeroed out
            # Update res if needed and reset lo/hi to 1 for next subarray
            if n == 0:
                res = max(res, n)
                lo, hi = 1, 1
                continue
            
            # Assess choices at each n and update res
            choices = (n, n*lo, n*hi)
            lo = min(choices)
            hi = max(choices)
            res = max(res, hi)

        return res

        
        
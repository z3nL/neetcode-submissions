class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        cl, ch = 1, 1
        for n in nums:
            if n==0:
                res = max(res,n)
                cl,ch = 1,1
                continue
            
            options = (n, n*cl, n*ch)
            cl = min(options)
            ch = max(options)
            res = max(res, ch)
            
        return res
        

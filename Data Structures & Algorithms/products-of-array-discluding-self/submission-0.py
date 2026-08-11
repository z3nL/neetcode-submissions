class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]

        post = [1]*n
        for i in range(n-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]
        
        return [pre[i]*post[i] for i in range (0,n)]
        
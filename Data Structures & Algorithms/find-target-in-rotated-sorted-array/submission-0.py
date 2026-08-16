class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        l, r = r, r+n-1
        while l <= r:
            m = (l+r)//2
            tm = m % n
            if nums[tm] < target:
                l = m+1
            elif nums[tm] > target:
                r = m-1
            else:
                return tm

        return -1
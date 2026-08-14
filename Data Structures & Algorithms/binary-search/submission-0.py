class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while (l < r):
            m = (l+r)//2
            c = nums[m]
            if c < target: l = m+1
            elif c > target: r = m
            else: return m
        return -1
        
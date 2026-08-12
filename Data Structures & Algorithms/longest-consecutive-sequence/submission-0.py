class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in nums:
            if n-1 in s:
                continue
            cur = 1
            j = n+1
            while j in s:
                cur += 1
                j += 1
            longest = max(cur, longest)
        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l = 0
        dude = set()
        for r in range(len(s)):
            while dude and s[r] in dude:
                dude.remove(s[l])
                l += 1
            res = max(res, r-l+1)
            dude.add(s[r])

        return res
        
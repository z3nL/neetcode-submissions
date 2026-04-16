class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def find(l,r):
            while l >= 0 and r < n and s[l]==s[r]:
                l -= 1
                r += 1
                self.res += 1

        for i in range(n):
            find(i,i)
            if i < n-1:
                find(i,i+1)
        return self.res
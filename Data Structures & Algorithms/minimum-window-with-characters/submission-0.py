class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0, float('inf')

        l = 0
        need = Counter(t)
        for r in range(len(s)):
            if s[r] in need: need[s[r]] -= 1
            while max(need.values()) == 0:
                if (r-l < j-i):
                    i, j = l , r
                if s[l] in need: need[s[l]] += 1
                l += 1

        return s[i:j+1] if j < float('inf') else ""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        bestL = 0
        bestR = 1
        bestLen = 0

        def find(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            l += 1

            return l, r, r-l+1

        for i in range(n-1):
            l1, r1, len1 = find(i, i)
            l2, r2, len2 = find(i, i+1)

            if len1 > len2 and len1 > bestLen:
                bestL, bestR, bestLen = l1, r1, len1
            elif len2 > len1 and len2 > bestLen:
                bestL, bestR, bestLen = l2, r2, len2
        
        return s[bestL:bestR]



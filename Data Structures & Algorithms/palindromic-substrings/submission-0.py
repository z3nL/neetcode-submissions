class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        # Is s[i:j] a palindrome
        dp = [[False]*n for _ in range(n)]

        # s[i:i] must be a palindrome
        for i in range(n):
            dp[i][i] = True
            res += 1
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 2:
                    dp[i][j] = s[i] == s[j] 
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                
                if dp[i][j]:
                    res += 1

        return res
        
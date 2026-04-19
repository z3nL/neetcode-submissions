class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # Can the suffix starting at s[i] be segmented?
        dp = [False]*(n+1)
        # The suffix starting at s[n] is empty
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                l = len(w)
                if i+l <= n and s[i:i+l] == w:
                    dp[i] = dp[i+l]
                    if dp[i]:
                        break


        # The solution
        return dp[0]
class Solution:
    def numDecodings(self, s: str) -> int:
        # The number of ways you can decode s[:i]
        n = len(s)
        dp = [0]*(n+1)

        # There is only one way to decode the empty string
        dp[0] = 1

        # Initialize for s[0]
        dp[1] = 1 if 1 <= int(s[0]) <= 9 else 0

        for i in range(2, n+1):
            # Is the current digit valid as a single
            one = 1 <= int(s[i-1]) <= 9
            # Is the current digit valid as part of a double
            two = 10 <= int(s[i-2:i]) <= 26

            # Inherit options from corresponding prefixes
            if one:
                dp[i] += dp[i-1]
            if two:
                dp[i] += dp[i-2]
        
        return dp[n]
        
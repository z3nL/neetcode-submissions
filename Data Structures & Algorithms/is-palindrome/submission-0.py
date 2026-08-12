class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = list()
        for c in s.lower():
            if c.isalnum():
                clean.append(c)
        return clean == list(reversed(clean))
        
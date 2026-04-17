class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = {}

        def wb(i):
            if i in cache:
                return cache[i]

            # Did we reach n without going over
            if i >= n:
                return True if i == n else False

            for w in wordDict: 
                l = len(w)
                if s[i:i+l] == w and wb(i+l):
                    cache[i] = True
                    return True
                    
            cache[i] = False
            return False
        
        return wb(0)
        
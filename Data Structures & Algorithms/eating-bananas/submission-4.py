class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def yeah(s):
            hrs = 0
            for p in piles:
                hrs += (p+s-1)//s
            return hrs <= h

        l, r = 1, max(piles)
        while l < r:
            m = (l+r)//2
            if yeah(m):
                r = m
            else:
                l = m + 1
        
        return l
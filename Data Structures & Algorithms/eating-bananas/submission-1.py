class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(piles, h, m):
            t = 0
            for p in piles:
                t += (p+m-1)//m
            return t <= h

        k = max(piles)

        l, r = 1, max(piles)

        while (l < r):
            m = (l+r)//2
            if can(piles, h, m):
                k = m
                r = m
            else:
                l = m+1

        return k
        
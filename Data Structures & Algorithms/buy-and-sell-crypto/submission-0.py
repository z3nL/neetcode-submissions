class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, res = float('inf'), 0
        for p in prices:
            lp = min(lp, p)
            res = max(p-lp, res)
        return res
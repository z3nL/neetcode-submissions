class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []
        for r in range(len(nums)):
            heapq.heappush(h, (-nums[r], r))
            while h[0][1] <= r-k:
                heapq.heappop(h)
            if r >= k-1:
                res.append(-h[0][0])

        return res
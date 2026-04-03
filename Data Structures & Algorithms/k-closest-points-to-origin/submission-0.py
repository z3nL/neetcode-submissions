class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            d = math.sqrt(x*x + y*y)
            heapq.heappush(h, (-d, x, y))
            if len(h) > k:
                heapq.heappop(h)
        
        return [[x,y] for d,x,y in h] if h else []
        
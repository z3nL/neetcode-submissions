class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n+1)]
        self.size = [1]*(n+1)
    
    def find(self, u):
        p = u
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        else:
            if self.size[v] < self.size[u]:
                pu, pv = pv, pu
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
            return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                distance = abs(xi-xj) + abs(yi-yj)
                tup = (distance, i, j)
                heapq.heappush(edges, tup)
        
        res = 0
        dsu = DSU(n)
        while edges:
            distance, u, v = heapq.heappop(edges)
            if dsu.union(u, v):
                res += distance
        return res

        
        
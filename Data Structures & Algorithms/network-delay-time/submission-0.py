class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        edges = defaultdict(list)
        seen = set()

        for u, v, t in times:
            edges[u].append((v, t))

        q = [(0, k)]
        while q:
            t1, u = heapq.heappop(q)
            if u in seen:
                continue
            seen.add(u)
            res = max(res, t1)
            for v, t2 in edges[u]:
                heapq.heappush(q, (t1+t2, v))

        return res if len(seen) == n else -1
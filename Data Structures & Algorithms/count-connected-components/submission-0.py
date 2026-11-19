class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        seen = set()

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def connect(cur, prev):
            if cur in seen:
                return
            seen.add(cur)
            for nxt in adj[cur]:
                if nxt != prev:
                    connect(nxt, cur)

        for cur in range(n):
            if cur in seen:
                continue
            connect(cur, None)
            res += 1
        return res

        
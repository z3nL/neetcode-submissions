class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        # Must reach every node without cycles
        def dfs(cur, prev):
            nonlocal n
            if cur in seen:
                return False
            seen.add(cur)
            n -= 1
            for nxt in adj[cur]:
                if nxt != prev and not dfs(nxt, cur):
                    return False
            return True
        return dfs(0, None) and n==0

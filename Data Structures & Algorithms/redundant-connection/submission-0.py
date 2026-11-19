class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        path = [1]
        res = None
        def dfs(cur, prev):
            nonlocal res

            if cur in seen:
                vals = set(path[path.index(cur):])
                for i in range(len(edges)-1, -1, -1):
                    if edges[i][0] in vals and edges[i][1] in vals:
                        res = edges[i]
                        return

            seen.add(cur)
            for nxt in adj[cur]:
                if nxt != prev:
                    path.append(nxt)
                    dfs(nxt, cur)
                    path.pop()
                    if res is not None:
                        return
        dfs(1, None)

        return res
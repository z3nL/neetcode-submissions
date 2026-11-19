class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        self.pacific = set()
        self.atlantic = set()

        for i in range(m):
            self.pacific.add((i,0))
            self.atlantic.add((i,n-1))
        for j in range(n):
            self.pacific.add((0,j))
            self.atlantic.add((m-1,j))

        def dfs(i, j, ocean):
            ocean.add((i,j))
            cur = heights[i][j]
            for dx,dy in ((-1,0), (0,-1), (0,1), (1,0)):
                if 0<=i+dx<m and 0<=j+dy<n\
                and (i+dx,j+dy) not in ocean and cur <= heights[i+dx][j+dy]:
                    dfs(i+dx, j+dy, ocean)

        for i, j in list(self.pacific):
            dfs(i, j, self.pacific)
        for i, j in list(self.atlantic):
            dfs(i, j, self.atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in self.pacific and (i,j) in self.atlantic:
                    res.append([i,j])
        return res
        

        
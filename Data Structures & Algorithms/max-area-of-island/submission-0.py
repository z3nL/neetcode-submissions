class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = -1

        m,n = len(grid), len(grid[0])

        def area(i, j):
            tmp = grid[i][j]
            grid[i][j] = 0
            if tmp != 1:
                return 0
            
            around = 0
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n:
                    around += area(ni, nj)
            
            return 1 + around


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, area(i,j))

        return max(res, 0)
        
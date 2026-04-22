class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        
        def explore(i, j):
            tmp = grid[i][j]
            grid[i][j] = 'X'
            if tmp != '1':
                return
            
            for dx, dy in [(-1,0), (1, 0), (0, 1), (0, -1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n:
                    explore(ni, nj)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    explore(i,j)
        return res
        
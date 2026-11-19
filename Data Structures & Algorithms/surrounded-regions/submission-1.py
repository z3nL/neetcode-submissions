class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        conversion_candidates = set()
        cancellation_sources = []

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'O':
                    continue
                conversion_candidates.add((i,j))
                if i in (0, m-1) or j in (0, n-1):
                    cancellation_sources.append((i,j))
        
        def dfs(i,j):
            conversion_candidates.remove((i,j))
            for dx, dy in ((-1,0), (0,-1), (0,1), (1,0)):
                if (
                    0<=i+dx<m
                    and 0<=j+dy<n
                    and (i+dx,j+dy) in conversion_candidates
                ):
                    dfs(i+dx, j+dy)

        for i, j in cancellation_sources:
            if (i,j) in conversion_candidates:
                dfs(i,j)
        for i, j in conversion_candidates:
            board[i][j] = 'X'
    
        
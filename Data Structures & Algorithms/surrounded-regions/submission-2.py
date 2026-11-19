class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        conversion_candidates = set()
        cancellation_queue = deque()

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'O':
                    continue
                conversion_candidates.add((i,j))
                if i in (0, m-1) or j in (0, n-1):
                    cancellation_queue.append((i,j))

        while cancellation_queue:
            i, j = cancellation_queue.popleft()
            if (i,j) not in conversion_candidates:
                continue
            conversion_candidates.remove((i,j))
            for dx,dy in ((-1,0),(0,-1),(0,1),(1,0)):
                if 0<=i+dx<m and 0<=j+dy<n:
                    cancellation_queue.append((i+dx, j+dy))
                    
        for i, j in conversion_candidates:
            board[i][j] = 'X'
    
        
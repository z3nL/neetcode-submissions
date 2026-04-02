class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        m, n = len(board), len(board[0])
        l = len(word)
        
        def find(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k+1 == l:
                return True
            
            tmp = board[i][j]
            board[i][j] = '#'
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n:
                    if find(ni, nj, k+1):
                        return True
            board[i][j] = tmp
            
            return False
        
        for i in range(m):
            for j in range(n):
                if find(i, j, 0):
                    return True
        
        return False
        
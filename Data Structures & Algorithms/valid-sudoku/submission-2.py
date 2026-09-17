class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                inRow = board[i][j] in rows[i]
                inCol = board[i][j] in cols[j]
                box = (i//3)*3 + (j//3)
                inBox = board[i][j] in boxes[box]
                if inRow or inCol or inBox:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[box].add(board[i][j])

        return True
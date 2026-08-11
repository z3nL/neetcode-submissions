class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                cur = board[i][j]
                if cur == '.':
                    continue
                box = (i // 3) * 3 + (j // 3)
                if (cur in rows[i] or cur in cols[j] or cur in boxes[box]):
                    return False
                rows[i].add(cur)
                cols[j].add(cur)
                boxes[box].add(cur)
        return True
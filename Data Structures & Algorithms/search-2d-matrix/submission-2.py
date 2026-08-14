class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        n = rows*cols
        l, r = 0, n
        while (l < r):
            m = (l+r)//2
            i, j = m // cols, m % cols
            if matrix[i][j] < target:
                l = m + 1
            elif matrix[i][j] > target:
                r = m
            else: return True
        return False
        
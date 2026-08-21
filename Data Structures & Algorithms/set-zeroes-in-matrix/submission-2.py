class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        rows = {}
        cols = {}
        row0 = False
        col0 = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(n):
            if i in rows:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(m):
            if j in cols:
                for i in range(n):
                    matrix[i][j] = 0
                    
        
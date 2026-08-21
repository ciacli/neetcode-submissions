class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        def isIn(i, j):
            return i >= 0 and i < n and j >= 0 and j < m
        row0 = False
        col0 = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        col0 = True
                    if i > 0 and j > 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
        #print(matrix)
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0
        #print(matrix)
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0
        #print(matrix)
        if row0 == True:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == True:
            for i in range(n):
                matrix[i][0] = 0
        
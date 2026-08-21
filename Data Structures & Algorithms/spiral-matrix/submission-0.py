class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        lowrow = 0
        uprow = n - 1
        lowcol = 0
        upcol = m - 1
        ans = []
        while (lowrow <= uprow) and (lowcol <= upcol):
            for j in range(lowcol, upcol + 1):
                ans.append(matrix[lowrow][j])
            lowrow += 1
            if lowrow > uprow: break
            for i in range(lowrow, uprow + 1):
                ans.append(matrix[i][upcol])
            upcol -= 1
            if lowcol > upcol: break
            for j in range(upcol, lowcol - 1, -1):
                ans.append(matrix[uprow][j])
            uprow -= 1
            if lowrow > uprow: break
            for i in range(uprow, lowrow - 1, -1):
                ans.append(matrix[i][lowcol])
            lowcol += 1
        return ans

                    
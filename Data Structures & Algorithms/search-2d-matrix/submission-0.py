class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lb = 0
        rowlen = len(matrix[0])
        collen = len(matrix)
        ub = rowlen * collen - 1
        while lb <= ub:
            mij = (lb + ub) // 2
            row = mij // rowlen
            col = mij % rowlen
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                ub = mij - 1
            else:
                lb = mij + 1
        return False
            

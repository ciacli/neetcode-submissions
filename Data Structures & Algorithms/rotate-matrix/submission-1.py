class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        low = 0
        up = n - 1
        while low <= up:
            first = low
            last = up
            while first < up:
                aux = matrix[last][low]
                matrix[last][low] = matrix[up][last]
                matrix[up][last] = matrix[first][up]
                matrix[first][up] = matrix[low][first]
                matrix[low][first] = aux
                first += 1
                last -= 1
            low += 1
            up -= 1

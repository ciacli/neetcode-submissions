from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        def isIn(i, j):
            return i >= 0 and i < n and j >= 0 and j < m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            i, j, dist = queue.popleft()
            dist += 1
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if isIn(ni, nj) and grid[ni][nj] == INF:
                    grid[ni][nj] = dist
                    queue.append((ni, nj, dist))
           

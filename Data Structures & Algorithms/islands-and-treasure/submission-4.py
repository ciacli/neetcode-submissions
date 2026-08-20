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
                    queue.append((i + 1, j, 1))
                    queue.append((i, j + 1, 1))
                    queue.append((i - 1, j, 1))
                    queue.append((i, j - 1, 1))
        while queue:
            i, j, dist = queue.popleft()
            if not isIn(i, j) or grid[i][j] != INF:
                continue
            
            grid[i][j] = dist
            dist += 1
            queue.append((i + 1, j, dist))
            queue.append((i, j + 1, dist))
            queue.append((i - 1, j, dist))
            queue.append((i, j - 1, dist))

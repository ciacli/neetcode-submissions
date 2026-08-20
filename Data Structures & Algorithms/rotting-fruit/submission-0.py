from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        d = {}
        def isIn(i, j):
            return i >= 0 and i < n and j >=0 and j < m
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    cnt += 1
                if grid[i][j] == 1:
                    cnt += 1
        ans = 0
        while queue:
            i, j, dist = queue.popleft()
            if not isIn(i, j) or grid[i][j] == 0 or (i, j) in d:
                continue 
            ans = max(ans, dist)
            dist += 1
            d[(i, j)] = 1
            cnt -= 1
            queue.append((i + 1, j, dist))
            queue.append((i, j + 1, dist))
            queue.append((i, j - 1, dist))
            queue.append((i - 1, j, dist))

        return ans if cnt == 0 else -1

        

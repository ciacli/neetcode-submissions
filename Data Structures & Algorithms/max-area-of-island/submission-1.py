class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = [0]
        def fill(cell_x, cell_y, cnt):
            nonlocal n
            nonlocal m
            nonlocal grid

            cnt[0] += 1
            grid[cell_x][cell_y] = 2
            if cell_x < n - 1 and grid[cell_x + 1][cell_y] == 1:
                fill(cell_x + 1, cell_y, cnt)
            if cell_x > 0 and grid[cell_x - 1][cell_y] == 1:
                fill(cell_x - 1, cell_y, cnt)
            if cell_y > 0 and grid[cell_x][cell_y - 1] == 1:
                fill(cell_x, cell_y - 1, cnt)
            if cell_y < m - 1 and grid[cell_x][cell_y + 1] == 1:
                fill(cell_x, cell_y + 1, cnt)
        ans = 0
        for i in range(n):
            for j in range(m):
                cnt[0] = 0
                if grid[i][j] == 1:
                    fill(i, j, cnt)
                ans = max(ans, cnt[0])
        return ans
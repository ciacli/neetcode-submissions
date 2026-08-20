class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def fill(cell_x, cell_y):
            nonlocal n
            nonlocal m
            nonlocal grid
            grid[cell_x][cell_y] = '2'
            if cell_x < n - 1 and grid[cell_x + 1][cell_y] == '1':
                fill(cell_x + 1, cell_y)
            if cell_x > 0 and grid[cell_x - 1][cell_y] == '1':
                fill(cell_x - 1, cell_y)
            if cell_y > 0 and grid[cell_x][cell_y - 1] == '1':
                fill(cell_x, cell_y - 1)
            if cell_y < m - 1 and grid[cell_x][cell_y + 1] == '1':
                fill(cell_x, cell_y + 1)
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    fill(i, j)
        return cnt

        
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def isIn(i, j):
            return i >= 0 and i < n and j >= 0 and j < m
        n = len(board)
        m = len(board[0])
        queue = deque()
        for i in range(n):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][m - 1] == 'O':
                queue.append((i, m - 1))
        for j in range(m):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[n - 1][j] == 'O':
                queue.append((n - 1, j))
        while queue:
            i, j = queue.popleft()
            board[i][j] = '1'
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j+ 1), (i, j - 1)):
                if isIn(ni, nj) and board[ni][nj] == 'O':
                    queue.append((ni, nj))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '1':
                    board[i][j] = 'O'
                 

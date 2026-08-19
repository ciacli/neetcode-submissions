class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        ans = False
        taken = {}
        def isIn(coords):
            return coords[0] >= 0 and coords[1] >= 0 and coords[0] < n and coords[1] < m

        def dfs(coords, idx, path):
            nonlocal ans
            if idx >= len(word):
                print(path)
                ans = True
                return True
            if not isIn(coords):
                return
            if board[coords[0]][coords[1]] != word[idx]:
                return
            
            taken[coords] = True
            path.append(coords)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if taken.get((coords[0] + i, coords[1] + j), False) == True or (i * j != 0):
                        continue
                    dfs((coords[0] + i, coords[1] + j), idx + 1, path)
            taken[coords] = False
            path.pop()


        for i in range(n):
            for j in range(m):
                dfs((i, j), 0, [])
                if ans == True:
                    return ans
        return ans
            

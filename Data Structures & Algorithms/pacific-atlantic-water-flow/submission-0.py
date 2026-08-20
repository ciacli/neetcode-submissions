class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = {}
        atlantic = {}
        n = len(heights)
        m = len(heights[0])
        def isIn(i, j):
            return i >= 0 and j >= 0 and i < n and j < m
        def dfs(i, j, d):
            if (i, j) in d:
                return 
            d[(i, j)] = 1
            for ni, nj in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if isIn(ni, nj) and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, d)

        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m - 1, atlantic)
        for j in range(m):
            dfs(0, j, pacific)
            dfs(n - 1, j, atlantic)
        ans = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append((i, j))
        return ans

        
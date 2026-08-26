class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sums = [0] * n
        sums[n - 1] = piles[n - 1]
        seen = {}
        for i in range(n - 2, -1, -1):
            sums[i] = sums[i + 1] + piles[i]
        def game(index, m):
            if index >= n:
                return 0
            if (index, m) in seen:
                return seen[(index, m)]
            seen[(index, m)] = -1
            for i in range(index, index + 2 * m):
                if i >= n: break
                candidate = sums[index] - game(index = i + 1, m = max(m, i - index + 1))
                seen[(index, m)] = max(seen[(index, m)], candidate)
            return seen[(index, m)]

        return game(0, 1)
                
        
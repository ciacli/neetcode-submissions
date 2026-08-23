class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        incoming = [[] for _ in range(n)]
        for s, d, p in flights:
            incoming[d].append([s, p])
        d = {}
        def dfs(node, k):
            if k <= 0:
                return -1
            if node == src:
                return 0
            if (node, k) in d:
                return d[(node, k)]
            d[(node, k)] = -1
            for s, p in incoming[node]:
                toSrc = dfs(s, k - 1)
                if toSrc == -1: continue

                if d[(node, k)] == -1 or d[(node, k)] > toSrc + p:
                    d[(node, k)] = toSrc + p

            return d[(node, k)]

        ans = dfs(dst, k + 2)
        print(d)
        return ans


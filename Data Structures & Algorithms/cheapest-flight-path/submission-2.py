class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        neighbors = [[] for _ in range(n)]
        for s, d, p in flights:
            neighbors[s].append([d, p])
        d = [INF] * n
        d[src] = 0
        for _ in range(k + 1):
            tmp = d[:]
            for node in range(n):
                for neighbor, p in neighbors[node]:
                    if tmp[neighbor] > d[node] + p:
                        tmp[neighbor] = d[node] + p
            d = tmp
        return d[dst] if d[dst] < INF else -1      
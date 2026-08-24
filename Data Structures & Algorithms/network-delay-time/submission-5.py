from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        d = [INF] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        d[k] = 0
        h = [(0, k)]
        for ui, vi, ti in times:
            adj[ui].append([vi, ti])
        while h:
            time, node = heapq.heappop(h)
            if time != d[node]:
                continue
            for vi, ti in adj[node]:
                if d[vi] > d[node] + ti:
                    d[vi] = d[node] + ti
                    heapq.heappush(h, (d[vi], vi))
        ans = max(d[1:])
        return ans if ans < INF else -1
            
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        d = [INF] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        d[k] = 0
        queue = deque()
        queue.append((k, 0))
        for ui, vi, ti in times:
            adj[ui].append([vi, ti])
        while queue:
            node, time = queue.popleft()
            if time != d[node]:
                continue
            for vi, ti in adj[node]:
                if d[vi] > d[node] + ti:
                    d[vi] = d[node] + ti
                    queue.append((vi, d[vi]))
        ans = max(d[1:])
        return ans if ans < INF else -1
            
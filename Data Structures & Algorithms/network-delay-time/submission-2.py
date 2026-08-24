from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        d = [INF] * (n + 1)
        n = [[] for _ in range(n + 1)]
        seen = {}
        d[k] = 0
        seen[k] = 1
        queue = deque()
        queue.append(k)
        for ui, vi, ti in times:
            n[ui].append([vi, ti])
        while queue:
            node = queue.popleft()
            for vi, ti in n[node]:
                ##continue
                if d[vi] > d[node] + ti:
                    seen[vi] = 1
                    d[vi] = d[node] + ti
                    queue.append(vi)
        ans = max(d[1:])
        return ans if ans < INF else -1
            
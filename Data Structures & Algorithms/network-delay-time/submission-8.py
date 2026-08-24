from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        d = [INF] * (n + 1)
        d[k] = 0
        for _ in range(n - 1):
            for ui, vi, ti in times:
                if d[vi] > d[ui] + ti:
                    d[vi] = d[ui] + ti
        ans = max(d[1:])
        return ans if ans < INF else -1

            
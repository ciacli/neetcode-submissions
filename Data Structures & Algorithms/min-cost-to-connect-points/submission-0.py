import numpy as np
import heapq
from collections import deque
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = [[] for _ in range(n)]
        s = set((list)(range(1, n)))
        h = []
        for i in range(n):
            for j in range(i + 1, n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                dist = np.abs(x1 - x2) + np.abs(y1 - y2)
                d[i].append((dist, j))
                d[j].append((dist, i))
        
        for elem in d[0]:
            heapq.heappush(h, elem)
        ans = 0
        while h:
            tp = heapq.heappop(h)
            #print(tp)
            dist = tp[0]
            elem  = tp[1]
            if elem not in s:
                continue
            s.remove(elem)
            ans += (int)(dist)
            for neighbor in d[elem]:
                heapq.heappush(h, neighbor)
        return ans
import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return np.sqrt(x**2 + y**2)
        h = []
        for point in points:
            x = point[0]
            y = point[1]
            if len(h) < k:
                heapq.heappush(h, (-dist(x, y), x, y))
            elif len(h) == k and dist(x, y) < (-h[0][0]):
                heapq.heappop(h)
                heapq.heappush(h, (-dist(x, y), x, y))
        return [t[1:] for t in h]
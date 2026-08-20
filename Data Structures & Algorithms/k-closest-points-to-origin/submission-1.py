import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return np.sqrt(x**2 + y**2)
        h = []
        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(h, (-dist(x, y), x, y))
            if len(h) > k:
                heapq.heappop(h)
                
                
        return [t[1:] for t in h]
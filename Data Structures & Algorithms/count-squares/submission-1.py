class CountSquares:

    def __init__(self):
        self.d = {}
    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.d[point] = self.d.get(point, 0) + 1
    def count(self, point: List[int]) -> int:
        ans = 0
        for corner in self.d.keys():
            if abs(corner[0] - point[0]) != abs(corner[1] - point[1]): continue
            if (corner[0] == point[0]) and (corner[1] == point[1]): continue
            val1 = self.d[corner]
            val2 = self.d.get((point[0], corner[1]), 0)
            val3 = self.d.get((corner[0], point[1]), 0)
            ans += val1 * val2 * val3
        return ans
            

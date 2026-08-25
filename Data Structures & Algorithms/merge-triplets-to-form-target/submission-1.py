class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = 0, 0, 0
        for a, b, c in triplets:
            if max(x, a) <= target[0] and max(y, b) <= target[1] and max(z, c) <= target[2]:
                x = max(x, a)
                y = max(y, b)
                z = max(z, c)
        return [x, y, z] == target
        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        n = len(stones)
        first = -1
        second = -1
        for _ in range(n - 1):       
            first = -heapq.heappop(h)
            second = -heapq.heappop(h)
            #print(str(first) + ' ' + str(second))
            res = abs(first - second)
            heapq.heappush(h, -res)
        return -h[-1]
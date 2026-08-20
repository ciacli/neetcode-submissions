class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for num in nums:
            if len(self.h) >= self.k:
                if self.h[0] <= num:
                    heapq.heappop(self.h)
                    heapq.heappush(self.h, num)
            else:
                heapq.heappush(self.h, num)

    def add(self, val: int) -> int:
        if len(self.h) >= self.k:
            if self.h[0] <= val:
                heapq.heappop(self.h)
                heapq.heappush(self.h, val)
        else:
            heapq.heappush(self.h, val)
        return self.h[0]
        

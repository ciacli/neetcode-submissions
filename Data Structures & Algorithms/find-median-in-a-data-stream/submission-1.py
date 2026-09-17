class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.count = 0
        

    def addNum(self, num: int) -> None:
        self.count += 1
        if self.maxHeap and -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        while len(self.maxHeap) - len(self.minHeap) > 1:
            top = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, top)
        while len(self.minHeap) - len(self.maxHeap) > 1:
            top = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -top)

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            return -self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        else: 
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
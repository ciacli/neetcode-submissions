import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                if h[0] < num:
                    heapq.heappop(h)
                    heapq.heappush(h, num)
        return h[0]
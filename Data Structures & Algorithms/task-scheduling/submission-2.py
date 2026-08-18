from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        queue = deque()
        d = [0] * 26

        for task in tasks:
            d[ord(task) - ord('A')] += 1
        for freq in d:
            if freq > 0:
                heapq.heappush(h, -freq)
        step = 0
        while h or queue:
            while queue and queue[0][1] + n < step:
                freq, _ = queue.popleft()
                heapq.heappush(h, -freq)
                
            if h:
                top = -heapq.heappop(h)
                top -= 1
                if top > 0:
                    queue.append((top, step))
            step += 1
        return step


        
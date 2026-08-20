class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        both = list(zip(position, speed))
        both.sort(key = lambda t: -t[0])
        for (pos, speed) in both:
            time = (target - pos) / speed
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
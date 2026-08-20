class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(0, len(height)):
            if len(stack) == 0 or height[stack[-1]] > height[i]:
                stack.append(i)
            if height[stack[-1]] <= height[i]:
                prev = stack.pop()
                while len(stack) > 0 and height[stack[-1]] <= height[i]:
                    ans += (height[stack[-1]] - height[prev]) * (i - stack[-1] -1)
                    prev = stack.pop()
                if len(stack) > 0:
                    ans += (height[i] -  height[prev]) * (i - stack[-1] - 1)
                stack.append(i)
        return ans

            
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights.append(0)
        stack = []
        canAppend = False
        enable = False

        for i, height in enumerate(heights):
             if not stack or heights[stack[-1]] < height:
                stack.append(i)
             else:
                ub = stack[-1]
                best = 0
                while stack and heights[stack[-1]] >= height:
                    idx = stack.pop()
                    lb = stack[-1] if stack else -1
                    best = max(best, heights[idx] * (i - lb - 1))

                stack.append(i)
                ans = max(ans, best)

             #print(ans)
        print(stack)
        return ans
                



        
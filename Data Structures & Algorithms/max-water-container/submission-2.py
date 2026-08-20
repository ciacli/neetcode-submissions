class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cnt = 0
        ans = 0
        lb = 0
        ub = len(heights) -1 
        while lb < ub:
            volume = min(heights[lb], heights[ub]) * (ub - lb)
            ans = max(ans, volume)
            if heights[lb] < heights[ub]:
                lb += 1
            else:
                ub -= 1
        return ans
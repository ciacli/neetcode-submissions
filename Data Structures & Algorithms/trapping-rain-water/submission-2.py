class Solution:
    def trap(self, height: List[int]) -> int:
        lb = 0
        ub = len(height) - 1
        ans = 0
        staple = 0
        while lb < ub:
            if height[lb] < height[ub]:
                staple = max(staple, height[lb])
                lb += 1
                ans += max(staple - height[lb], 0)
            else:
                staple = max(staple, height[ub])
                ub -= 1
                ans += max(staple - height[ub], 0)
        return ans

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        lb, ub = 0, 0
        n = len(nums)
        while ub < n - 1:
            M = 0
            while lb <= ub:
                M = max(nums[lb] + lb, M)
                lb += 1
            ub = M
            ans += 1
        return ans

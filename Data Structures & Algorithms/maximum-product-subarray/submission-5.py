class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        Min = nums[0]
        Max = nums[0]
        for num in nums[1:]:
            candidates = (num, Min * num, Max * num)
            Min = min(candidates)
            Max = max(candidates)
            ans = max(ans, Max)
        return ans
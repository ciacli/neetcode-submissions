class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = (n * (n + 1)) // 2
        for num in nums:
            ans -= num
        return ans
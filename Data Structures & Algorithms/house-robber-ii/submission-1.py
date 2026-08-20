class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(2)]
        dp[1][0] = nums[0]
        dp[0][0] = 0
        if n > 1:
            dp[0][1] = nums[1]
            dp[1][1] = max(nums[0], nums[1])

        for i in range(2, n - 1):
            dp[0][i] = max(nums[i] + dp[0][i - 2], dp[0][i - 1])
            dp[1][i] = max(nums[i] + dp[1][i - 2], dp[1][i -1])

        before = dp[0][n - 3] if n > 2 else 0
        otherwise = dp[1][n - 2] if n > 1 else 0
        return max(nums[n - 1] + before, otherwise)
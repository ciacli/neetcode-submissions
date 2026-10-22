class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2:
            return False
        dp = [[False] * (s // 2 + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        for i in range(n):
            for j in range(nums[i], s // 2 + 1):
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]

        return dp[n - 1][s // 2]
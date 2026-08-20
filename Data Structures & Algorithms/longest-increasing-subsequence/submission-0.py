class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            mx = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    mx = max(mx, dp[j])
            dp[i] = mx + 1
            dp[i] = mx + 1
        ans = max(dp)
        #print(dp)
        return ans
            
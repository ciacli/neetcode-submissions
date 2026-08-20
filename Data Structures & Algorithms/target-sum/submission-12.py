import numpy as np
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target:
            return 0
        n = len(nums)
        dp = [[0] * (2 * total + 1) for _ in range(2)]
        # zero is in the middle everything left is negative and everything right is positive
        zeroPos = total
        dp[1][zeroPos + nums[0]] += 1
        dp[1][zeroPos - nums[0]] += 1
        for i, num in enumerate(nums):
            if i == 0:
                continue
            dp[0] = dp[1]
            dp[1] = [0] * (2 * total + 1)
            for sm in range(total + 1):
                a = dp[0][zeroPos + (sm - num)] if sm - num >= -total else 0
                b = dp[0][zeroPos + (sm + num)] if sm + num <= total else 0
                dp[1][zeroPos + sm] = a + b

                a = dp[0][zeroPos + (sm + num)] if sm + num <= total else 0
                b = dp[0][zeroPos - (sm - num)] if sm - num >= -total else 0
                dp[1][zeroPos - sm] = a + b
        return dp[1][zeroPos + target]

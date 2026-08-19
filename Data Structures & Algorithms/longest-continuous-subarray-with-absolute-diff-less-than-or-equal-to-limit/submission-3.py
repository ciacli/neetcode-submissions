from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = 0
        lb = 0
        for ub in range(n):
            tmp = lb - 1
            for i in range(lb, ub):
                if abs(nums[i] - nums[ub]) > limit:
                    tmp = i
            lb = tmp + 1
            ans = max(ans, ub - lb + 1)
        return ans
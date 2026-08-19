from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = 0
        mins = deque()
        maxes = deque()
        lb = 0
        for ub in range(n):
            while mins and nums[mins[-1]] > nums[ub]:
                mins.pop()
            mins.append(ub)

            while maxes and nums[maxes[-1]] < nums[ub]:
                maxes.pop()
            maxes.append(ub)

            while maxes and mins and nums[maxes[0]] - nums[mins[0]] > limit:
                if maxes[0] < mins[0]:
                    lb = maxes.popleft() + 1
                else:
                    lb = mins.popleft() + 1

            ans = max(ans, ub - lb + 1)
            #print(str(lb) + ' ' + str(ub) +  ' ' + str(mins) + ' ' + str(maxes) + ' ' + str(ans))
        return ans
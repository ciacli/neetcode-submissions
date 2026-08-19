class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        def back(start, res):
            ans.append(res[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                res.append(nums[i])
                back(i + 1, res)
                res.pop()
        back(0, [])
        return ans


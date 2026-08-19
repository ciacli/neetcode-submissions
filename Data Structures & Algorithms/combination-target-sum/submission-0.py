class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        def back(start, total, res):
            nonlocal target
            nonlocal n
            nonlocal ans
            if total == target:
                ans.append(res[:])
                return
            for i in range(start, n):
                if total + nums[i] > target:
                    continue
                res.append(nums[i])
                back(i, total + nums[i], res)
                res.pop()
        back(0, 0, [])
        return ans

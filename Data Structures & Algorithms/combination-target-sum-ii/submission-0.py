class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(candidates)
        n = len(nums)
        nextIdx = {}
        for i in range(n):
            if i == n - 1 or nums[i] != nums[i + 1]:
                nextIdx[nums[i]] = i + 1
        print(nextIdx)

        def back(start, total, res):
            nonlocal target
            nonlocal n
            nonlocal ans
            nonlocal nextIdx
            if total == target:
                ans.append(res[:])
                return
            i = start
            while i < n:
                if total + nums[i] <= target:
                    res.append(nums[i])
                    back(i + 1, total + nums[i], res)
                    res.pop()
                i = nextIdx[nums[i]]
        back(0, 0, [])
        return ans
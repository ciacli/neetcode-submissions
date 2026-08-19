class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        appeared = [0] * n
        ans = []
        def back(l, res):
            if l == n:
                ans.append(res[:])
                return
            for i in range(n):
                if appeared[i] == 1:
                    continue
                res.append(nums[i])
                appeared[i] = 1
                back(l + 1, res)
                res.pop()
                appeared[i] = 0
        back(0, [])
        return ans
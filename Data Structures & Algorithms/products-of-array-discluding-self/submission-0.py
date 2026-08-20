class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        l = len(nums)
        ans = [1] * l
        for i in range(1, l):
            p *= nums[i - 1]
            ans[i] *= p
        p = 1
        for i in range(l-2, -1, -1):
            p *= nums[i + 1]
            ans[i] *= p
        return ans            

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        prod1 = 1
        prod2 = 1
        start = 0
        for num in nums:
            if start: 
                prod2 *= num
                ans = max(ans, prod2)
            prod1 *= num
            ans = max(ans, prod1)
            if prod1 < 0:
                start = 1
            if num == 0:
                prod1, prod2, start = 1,1,0
        return ans
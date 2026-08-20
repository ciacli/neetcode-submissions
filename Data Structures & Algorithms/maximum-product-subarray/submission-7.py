class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        pref = 1
        suf = 1
        for num in nums:
            pref *= num
            if pref == 0:
                pref = num
            ans = max(ans, pref)
        
        for num in nums[:: -1]:
            print(suf)
            suf *= num 
            if suf == 0:
                suf = num
            ans = max(ans, suf)
        return ans
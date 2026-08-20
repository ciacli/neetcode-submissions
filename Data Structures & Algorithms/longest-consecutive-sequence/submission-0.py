class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        freq = {}
        for num in nums:
            freq[num] = 1
            
        ans = 0
        cnt = 0
        for i in range(0, len(nums)):
            if freq.get(nums[i] - 1, 0) == 1:
                continue
            j = nums[i]
            while freq.get(j, 0) == 1:
                cnt += 1
                j  += 1
            ans = max(cnt, ans)
            cnt = 0

        return ans
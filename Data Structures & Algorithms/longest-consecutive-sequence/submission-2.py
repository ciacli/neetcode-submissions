class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        freq = {}
        for num in nums:
            freq[num] = 1
            
        ans = 0
        cnt = 0
        for num in freq.keys():
            if freq.get(num - 1, 0) == 1:
                continue
            j = num
            while freq.get(j, 0) == 1:
                cnt += 1
                j  += 1
            ans = max(cnt, ans)
            cnt = 0

        return ans
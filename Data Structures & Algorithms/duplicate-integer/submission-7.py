class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqs = {}
        for num in nums: 
            if freqs.get(num, 0) == 1:
                return True
            else:
                freqs[num] = 1
        return False
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max = count if count > max else max
                count = 0
        max = count if count > max else max
        return max
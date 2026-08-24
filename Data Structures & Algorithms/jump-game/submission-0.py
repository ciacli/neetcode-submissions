class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        n = len(nums)
        for pos, dist in enumerate(nums):
            if pos > furthest: 
                return False
            furthest = max(furthest, pos + dist)
            if furthest >= n - 1:
                return True
        return furthest >= n - 1
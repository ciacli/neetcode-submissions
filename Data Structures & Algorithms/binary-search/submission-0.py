class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        while lb <= ub:
            mij = (lb + ub) // 2
            if nums[mij] == target:
                return mij 
            elif nums[mij] > target:
                ub = mij - 1
            else: lb = mij + 1
        return -1
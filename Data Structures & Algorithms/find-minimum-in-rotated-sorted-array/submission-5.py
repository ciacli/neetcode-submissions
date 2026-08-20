class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb = 0
        l = len(nums)
        ub = l - 1
        while lb < ub:
            mid = (lb + ub) // 2
            if nums[mid] > nums[ub]:
                lb = mid + 1
            else:
                ub = mid
        return nums[lb]
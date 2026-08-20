class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        while lb <= ub:
            mid = (lb + ub) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                if nums[mid] < nums[ub] and target > nums[ub]:
                    ub = mid - 1
                else:
                    lb = mid + 1
                
            else:
                if nums[mid] > nums[ub] and target <= nums[ub]:
                    lb = mid + 1
                else:
                    ub = mid - 1
        return -1
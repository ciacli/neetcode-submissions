class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0
        ub = len(nums) - 1
        #there must be at least one half that is sorted so we have to identify it
        while lb <= ub:
            mid = (lb + ub) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < nums[ub]: #right half is sorted
                if nums[mid] < target <= nums[ub]:
                    lb = mid + 1
                else:
                    ub = mid - 1
            else: #left half is sorted
                if nums[mid] > target >= nums[lb]:
                    ub = mid - 1
                else:
                    lb = mid + 1
           
        return -1
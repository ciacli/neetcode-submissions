class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lb = 0
        l = len(nums)
        ub = l - 1
        ans = 0
        while lb <= ub:
            mid = (lb + ub) // 2
            if (mid == l - 1 or nums[mid] != nums[mid + 1]) and (mid == 0 or nums[mid] != nums[mid - 1]):
                ans = nums[mid]
            if ((mid == l - 1 or nums[mid] == nums[mid + 1]) and mid % 2== 1) or ((mid == 0 or nums[mid] == nums[mid - 1]) and mid % 2 == 0):
                ub = mid - 1
            else:
                lb = mid + 1
        return ans
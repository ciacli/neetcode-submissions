class Solution:
    def findMin(self, nums: List[int]) -> int:
        lb = 0
        l = len(nums)
        ub = l - 1
        ans = nums[0]
        while lb <= ub:
            mid = (lb + ub) // 2
            print(mid)
            ans = min(ans, nums[mid])
            if nums[mid] > nums[ub]:
                lb = mid + 1
            else:
                ub = mid - 1
        return ans
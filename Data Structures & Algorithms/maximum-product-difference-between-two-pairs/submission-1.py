class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mins = [-1] * 2
        maxs = [-1] * 2
        for i, num in enumerate(nums):
            if nums[maxs[0]] < num or maxs[0] == -1:
                maxs[0] = i
            if nums[mins[0]] > num or mins[0] == -1:
                mins[0] = i
        for i, num in enumerate(nums):
            if i != maxs[0]:
                if nums[maxs[1]] < num or maxs[1] == -1:
                    maxs[1] = i
            if i != mins[0]:
                if nums[mins[1]] > num or mins[1] == -1:
                    mins[1] = i
        print(maxs)
        print(mins)
        return (nums[maxs[0]] * nums[maxs[1]]) - (nums[mins[0]] * nums[mins[1]])
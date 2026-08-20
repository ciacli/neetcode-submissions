class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            newTarget = target - num
            if d.get(newTarget, -1) != -1:
                return [d[newTarget], index]
            else:
                d[num] = index
        return []
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        d = {}
        for index in range(0, len(nums)):
            lb = index + 1
            ub = len(nums) - 1
            while lb < ub:
                if nums[lb] + nums[ub] == -nums[index]:
                    combo = [nums[lb], nums[ub], nums[index]]
                    key = tuple(sorted(combo))
                    if d.get(key, 0) == 0:
                        ans.append(combo)
                        d[key] = 1
                    lb += 1
                    ub -= 1
                elif nums[lb] + nums[ub] > -nums[index]:
                    ub -= 1
                else:
                    lb +=1
        return ans

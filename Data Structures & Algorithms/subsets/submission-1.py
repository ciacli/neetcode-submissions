class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        n = len(nums)

        def back(cur, k):
            nonlocal ans
            nonlocal nums
            ans.append(cur[:])
            for i in range(k, n):
                cur.append(nums[i])
                back(cur, i + 1)
                cur.pop() 

        back(cur, 0)
        return ans

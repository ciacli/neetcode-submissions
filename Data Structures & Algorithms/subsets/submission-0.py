class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        n = len(nums)

        def back(cur, k):
            nonlocal ans
            nonlocal nums
            ans.append(cur[:])
            for i in range(n):
                if (not cur) or (k < i):
                    cur.append(nums[i])
                    back(cur, i)
                    cur.pop() 

        back(cur, 0)
        return ans

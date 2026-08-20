class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 
        mask = 1
        for shift in range(32):
            ans += ((n >> shift) & 1) | 0
        return ans

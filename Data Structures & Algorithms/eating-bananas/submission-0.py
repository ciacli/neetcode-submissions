class Solution:
    def valid(self, rate, piles, h):
        cnt = 0
        for pile in piles:
            cnt += pile // rate + ((pile % rate) > 0)
        return cnt <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lb = 1
        ub = 0
        ans = 0
        for pile in piles:
            ub = max(ub, pile)
        while lb <= ub:
            mij = (lb + ub) // 2
            if self.valid(mij, piles, h) == True:
                ans = mij
                ub = mij - 1
            else:
                lb = mij + 1
        return ans

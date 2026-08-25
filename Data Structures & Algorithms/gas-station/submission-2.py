class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        total = 0
        ans = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(n):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                ans = i + 1
        return ans


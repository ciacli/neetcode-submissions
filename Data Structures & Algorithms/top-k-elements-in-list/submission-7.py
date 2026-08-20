
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        best = [0] * k
        filled = 0
        isContained = {}
        for num in nums:
            d.setdefault(num, 0)
            d[num] += 1
            if filled < k:
                if isContained.setdefault(num, 0) == 0:
                    best[filled] = num    
                    filled += 1
                    isContained[num] = 1

            else:
                toReplace = -1
                if isContained.setdefault(num, 0) == 0:
                    for index, elem in enumerate(best):
                        if d[elem] < d[num]:
                            if toReplace == -1 or d[best[toReplace]] > d[elem]:
                                toReplace = index
                    if toReplace != -1:
                        isContained[best[toReplace]] = 0
                        isContained[num] = 1
                        best.pop(toReplace)
                        best.append(num)
                            
        return best
                

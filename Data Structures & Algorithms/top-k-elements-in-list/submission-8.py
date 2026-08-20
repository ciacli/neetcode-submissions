import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        best = {}
        ans = []
        max = 0
        total = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, freq in freq.items():
            best.setdefault(freq, []).append(num)
            if freq > max:
                max = freq
        for i in range(max, 0, -1):
            ans.append(best.get(i, []))
        ans = np.concatenate(ans).tolist()
        return ans[:k]

                    
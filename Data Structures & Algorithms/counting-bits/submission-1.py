class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        shift = 0
        maxpow = 0
        output[0] = 0
        for i in range(1, n + 1):
            if i == 1 << shift:
                maxpow = i
                shift += 1
            output[i] = 1 + output[i - maxpow]
        return output
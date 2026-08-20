from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            cnt = tuple(sorted(Counter(string).items()))
            d.setdefault(cnt, []).append(string)
        return list(d.values())
            
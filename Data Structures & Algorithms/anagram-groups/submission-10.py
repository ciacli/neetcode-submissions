from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            cnt = [0] * 26
            for c in string:
                cnt[ord(c) - ord("a")] += 1
            key = tuple(cnt)
            d.setdefault(key, []).append(string)
        return list(d.values())
            
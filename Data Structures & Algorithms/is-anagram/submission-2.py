from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(t) == Counter(s):
            return True
        return False
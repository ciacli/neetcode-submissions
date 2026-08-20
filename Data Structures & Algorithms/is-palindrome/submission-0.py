class Solution:
    def isPalindrome(self, s: str) -> bool:
        lb = 0
        ub = len(s) - 1
        while lb <= ub:
            if s[lb].isalnum() == False:
                lb += 1
                continue
            elif s[ub].isalnum() == False:
                ub -= 1
                continue
            first = s[lb].lower()
            last = s[ub].lower()
            if first != last:
                return False
            lb += 1
            ub -= 1
        return True

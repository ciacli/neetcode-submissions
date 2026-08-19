class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        ans = []
        d = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def back(start, res):
            if start == n:
                if res:
                    ans.append(res[:])
                return
            options = d[digits[start]]
            for option in options:
                back(start + 1, res + option)
        back(0, "")
        return ans
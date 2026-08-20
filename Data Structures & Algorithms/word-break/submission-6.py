class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
        
        for lb in range(len(s)):
            for ub in range(lb, min(lb + maxlen, len(s))):
                beforeOK = dp[lb - 1] if lb >= 1 else True
                if beforeOK & (s[lb : ub + 1] in wordDict):
                    dp[ub] = True  
        return dp[len(s) - 1]
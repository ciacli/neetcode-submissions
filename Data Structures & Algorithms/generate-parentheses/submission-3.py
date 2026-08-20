class Solution:
    def back(self, nopen: int, nclosed : int, string: str, ans: List[str]):
        if nopen == 0 and nclosed == 0:
            ans.append(string)
        if nclosed < nopen:
            return
        if nopen > 0: 
            self.back(nopen - 1, nclosed, string + "(", ans)
        if nclosed > 0:
            self.back(nopen, nclosed - 1, string + ")", ans)
        
            
    def valid(self, string: str) -> bool:
        stack = []
        for c in string:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.back(n, n, "", ans)
        return ans
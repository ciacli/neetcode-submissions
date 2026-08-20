class Solution:
    def back(self, nopen: int, nclosed : int, string: str, ans: List[str]):
        if nopen == 0 and nclosed == 0:
            self.validAndAppend(string, ans)
        if nopen > 0: 
            self.back(nopen - 1, nclosed, string + "(", ans)
        if nclosed > 0:
            self.back(nopen, nclosed - 1, string + ")", ans)
        
            

    def validAndAppend(self, string: str, ans: List[str]):
        stack = []
        for c in string:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return
                stack.pop()
        ans.append(string)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.back(n, n, "", ans)
        return ans
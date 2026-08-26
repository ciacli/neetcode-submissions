class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == ')':
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
        
        while left:
            if stars:
                if stars[-1] > left[-1]:
                    stars.pop()
                    left.pop()
                else:
                    return False
            else:
                return False


        return True
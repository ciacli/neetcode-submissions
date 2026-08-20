class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                first = stack.pop()
                second = stack.pop()
                ans = first + second
                stack.append(ans)
            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                ans = second - first
                stack.append(ans)
            elif token == '*':
                first = stack.pop()
                second = stack.pop()
                ans = first * second
                stack.append(ans)
            elif token == '/':
                first = stack.pop()
                second = stack.pop()
                ans = second / first
                ans = int(ans)
                stack.append(ans)
            else:
                ans = 0
                neg = False
                for c in token:
                    if c == '-':
                        neg = True
                    else:
                        ans = ans * 10 + ord(c) - ord('0')
                if neg:
                    ans = -ans
                stack.append(ans)
        return stack[-1]


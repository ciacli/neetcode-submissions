class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def isPal(el):
            lb = 0
            ub = len(el) - 1
            while lb < ub:
                if el[lb] != el[ub]:
                    return False
                lb += 1
                ub -= 1
            return True

        def back(start, res):
            if start == n:
                ans.append(res[:])
                return
            for i in range(start, n):
                string = s[start: i + 1]
                if not isPal(string):
                    continue
                res.append(string) 
                back(i + 1, res)
                res.pop()
        back(0, [])
        return ans

                
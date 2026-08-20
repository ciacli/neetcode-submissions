class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for string in strs:
            encoded = str(len(string)) + '/' + string
            ans.append(encoded)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = 0
            while s[i] != '/':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i += 1
            i += 1
            ans.append("".join(s[i : i + length]))
            i += length
        return ans
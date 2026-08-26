class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        read = 0
        write = 0
        while read < n:
            c = chars[read]
            cnt = 0
            while read < n and chars[read] == c:
                cnt += 1
                read += 1
            chars[write] = c
            write += 1
            if cnt > 1:
                for d in str(cnt):
                    chars[write] = d
                    write += 1
        return write
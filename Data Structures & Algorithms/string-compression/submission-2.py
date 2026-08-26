class Solution:
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        aux = []
        cnt = 1
        i = 1
        k = 0
        while i < len(chars):
            
            if chars[i] == last:
                cnt += 1
            else:
                aux.append(last)
                k += 1
                last = chars[i]
                if cnt > 1:
                    nums = []
                    while cnt:
                        nums.append(str(cnt % 10))
                        k += 1
                        cnt = cnt // 10
                    for num in nums[::-1]:
                        aux.append(num)
                cnt = 1
            
            i += 1
                    
        aux.append(last)
        k += 1
        if cnt > 1:
            nums = []
            while cnt:
                nums.append(str(cnt % 10))
                k += 1
                cnt = cnt // 10
            for num in nums[::-1]:
                aux.append(num)

        i = 0
        while i < len(aux) and i < len(chars):
            chars[i] = aux[i]
            i += 1
        return k

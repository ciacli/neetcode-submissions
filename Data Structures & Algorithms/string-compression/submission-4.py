class Solution:
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        n = len(chars)
        aux = []
        cnt = 1
        i = 1
        k = 0
        while i < n:
            
            if chars[i] == last:
                cnt += 1
            else:
                chars[k] = last
                k += 1
                last = chars[i]
                if cnt > 1:
                    nums = []
                    while cnt:
                        nums.append(str(cnt % 10))
                        cnt = cnt // 10
                    for num in nums[::-1]:

                        chars[k] = num
                        k += 1
                cnt = 1
            
            i += 1
        
        
        chars[k] = last
        k += 1
        if cnt > 1:
            nums = []
            while cnt:
                nums.append(str(cnt % 10))
                cnt = cnt // 10
            for num in nums[::-1]:  
                chars[k] = num
                k += 1
        return k

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFF
        ans = 0
        carry = 0
        for i in range(12):
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1
            #print(str(bit1) + " " + str(bit2))
            res = (bit1 ^ bit2) ^ carry
            carry = (bit1 & carry) | (bit2 & carry) | (bit1 & bit2)
            print(str(bit1) + " " + str(bit2) + " " +str(res) + " " + str(carry))
            ans = ans | (res << i)
        if ans >> 11:
            ans = ~(ans ^ mask)
        return ans

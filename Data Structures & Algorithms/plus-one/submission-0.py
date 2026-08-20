class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = digits[:]
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            carry, ans[i] = (ans[i] + carry) // 10, (ans[i] + carry) % 10
            i -= 1
        return [carry] + ans if carry else ans
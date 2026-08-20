class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                aux = nums[i]
                nums[i] = nums[length - 1]
                nums[length - 1] = aux
                length -= 1
            else:
                i += 1
        return length
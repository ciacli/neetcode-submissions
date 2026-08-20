class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lb = 0
        ub = len(numbers) - 1
        while lb <= ub:
            first = numbers[lb]
            last = numbers[ub]
            if first + last == target:
                return [lb + 1, ub + 1]
            elif first + last > target:
                ub -= 1
            else:
                lb += 1
        return []
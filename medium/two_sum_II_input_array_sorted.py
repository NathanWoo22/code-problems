class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if target < numbers[left] + numbers[right]:
                right = right - 1
            else:
                left = left + 1
        
        return [left + 1, right + 1]

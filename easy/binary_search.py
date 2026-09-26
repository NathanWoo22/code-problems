class Solution:
    def search(self, nums: list[int], target: int) -> int:
        upper = len(nums) - 1
        lower = 0
        while lower <= upper:
            i = (upper + lower) // 2
            val = nums[i]
            if val < target:
                lower = i + 1
            elif val > target: 
                upper = i - 1
            else:
                return i
        return -1

class Solution:
    def findMin(self, nums: list[int]) -> int:
        upper = len(nums) - 1
        lower = 0
        while lower <= upper:
            mid = (upper + lower) // 2
            if nums[upper] >= nums[lower]:
                return nums[lower]
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[upper] < nums[mid]:
                lower = mid + 1
            elif nums[lower] > nums[mid]:
                upper = mid - 1

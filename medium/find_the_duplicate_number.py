class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        newSlow = 0
        while True:
            newSlow = nums[newSlow]
            fast = nums[fast]
            if newSlow == fast:
                return newSlow

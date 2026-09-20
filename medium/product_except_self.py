class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [1] 
        for i in range(len(nums)):
            prefix.append(prefix[i] * nums[i])

        for i in range(len(nums), 1, -1):
            suffix.append(nums[i-1] * suffix[len(nums) - i])

        returnList = []
        for i in range(len(nums)):
            returnList.append(prefix[i] * suffix[len(nums) - i -1])
        return returnList

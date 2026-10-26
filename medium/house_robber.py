class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxRob = [0] * len(nums)
        maxRob[0] = nums[0]
        maxRob[1] = nums[1]
        
        for i in range(2, len(nums)):
            if i - 3 >= 0:
                maxRob[i] = max(maxRob[i-3] + nums[i], maxRob[i-2] + nums[i])
            else:
                maxRob[i] = maxRob[i-2] + nums[i]

        return max(maxRob[-1], maxRob[-2])

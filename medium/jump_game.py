class Solution:
    def canJump(self, nums: list[int]) -> bool:

        # DP Solution:
        # canReachEnd = [False] * len(nums)
        # canReachEnd[-1] = True

        # for i in range(len(canReachEnd) - 1, -1, -1):
        #     # move backwards until we reach another space that can reach end
        #     curSpaces = 0
        #     while curSpaces + i < len(canReachEnd) and curSpaces <= nums[i]:
        #         if canReachEnd[curSpaces + i] == True:
        #             canReachEnd[i] = True
        #             break
        #         curSpaces += 1
            
        # return canReachEnd[0]

        # greedy approach
        # goal = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if i + nums[i] > len(nums) - 1 or i + nums[i] >= goal:
        #         goal = i

        # return goal == 0 

        # greedy aproach forward
        canReachIndex = 0
        for i in range(0, len(nums)):
            if i > canReachIndex:
                print(i)
                return False
            canReachIndex = max(canReachIndex, i + nums[i]) 
        return canReachIndex >= len(nums) - 1

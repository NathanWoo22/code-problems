class Solution:
    def jump(self, nums: list[int]) -> int:
        # Start at the first most position and keep going greedily until we get tehre
        # reachable = len(nums) - 1
        # jumpCount = 0 
        # while reachable > 0:
        #     for i in range(reachable):
        #         if nums[i] + i >= reachable:
        #             reachable = i
        #             break
        #     jumpCount += 1
        # return jumpCount

        # define ranges we can get to 
        l, r = 0, 0
        steps = 0
        while r < len(nums) - 1:
            newMax = nums[l] + l
            for i in range(l, r + 1):
                newMax = max(newMax, i + nums[i])
            l = r 
            r = newMax
            steps += 1
        return steps

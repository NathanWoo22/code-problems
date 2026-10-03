class Solution:
    def maxSlidingWindow(self, nums: list[intd], k: int) -> list[int]:
        q = deque()
        output = []

        for i, val in enumerate(nums):
            while q and val >= nums[q[-1]]:
                q.pop()

            q.append(i)

            if q and i - k + 1 > q[0]:
                q.popleft()

            if q and i - k + 1 >= 0: 
                output.append(nums[q[0]])
            
        return output

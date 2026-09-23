class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums) 
        results = []
        for i in range(len(nums)):
            target = -nums[i]
            left = i + 1 
            right = len(nums) - 1
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while True:
                if left >= right:
                    break
                
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                total = nums[right] + nums[left]
                if total < target:
                    left += 1
                    
                elif total > target:
                    right -= 1 

                elif nums[right] + nums[left] == target:
                    results.append([nums[left], nums[right], nums[i]])
                    right -= 1 
                    left += 1
                    while nums[left] == nums[right + 1] and left < right:
                        left += 1

                    

        return [list(x) for x in {tuple(y) for y in results}]
                

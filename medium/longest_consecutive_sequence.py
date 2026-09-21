class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)

        maxSeq = 0
        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                while num+count in numSet:
                    count += 1 
                
                maxSeq = max(count, maxSeq)
        
        return maxSeq

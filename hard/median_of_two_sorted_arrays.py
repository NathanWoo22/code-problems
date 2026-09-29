class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        smallArr = []
        bigArr = []
        totalLen = len(nums1) + len(nums2)
        totalMid = totalLen // 2
        if len(nums1) < len(nums2):
            smallArr = nums1
            bigArr = nums2
        else:
            smallArr = nums2
            bigArr = nums1
        
        l = 0
        r = len(smallArr) - 1
        
        while True: 
            mid = (l + r) // 2
            rem = totalMid - mid - 2
            if mid >= 0:
                smallLeft = smallArr[mid]
            else:
                smallLeft = float("-infinity")
            if mid < len(smallArr) - 1:
                smallRight = smallArr[mid + 1] 
            else:
                smallRight = float("infinity")
            if rem >= 0: 
                bigLeft = bigArr[rem]
            else:
                bigLeft = float("-infinity")
            if rem < len(bigArr) - 1:
                bigRight = bigArr[rem + 1]
            else:
                bigRight = float("infinity")
            if bigRight >= smallLeft and smallRight >= bigLeft: 
                if totalLen % 2 == 0:
                    return (max(bigLeft, smallLeft) + min(bigRight, smallRight)) / 2.0
                else:
                    return min(bigRight, smallRight)
            
            if bigRight < smallLeft:
                r = mid - 1
            else:
                l = mid + 1
            
        return -100

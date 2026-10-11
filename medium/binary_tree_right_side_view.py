# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        queue = [root]
        returnList = []

        while True:
            levelList = queue
            queue = []
            rightVal = None 
            for node in levelList:
                if node:
                    rightVal = node.val
                    queue.append(node.left)
                    queue.append(node.right)
                
            if rightVal != None:
                returnList.append(rightVal)
            else:
                return returnList
        
        return returnList

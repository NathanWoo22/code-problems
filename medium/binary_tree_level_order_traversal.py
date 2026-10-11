# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = []
        queue.append(root)
        returnList = []

        while True:
            levelNodes = queue
            queue = []
            levelList = []
            for node in levelNodes:
                if node:
                    levelList.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if levelList == []:
                return returnList
            returnList.append(levelList)
                          
        return returnList

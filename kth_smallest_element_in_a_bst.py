# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stack = []
        curNode = root  
        counter = 0

        while stack or curNode: 
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            
            curNode = stack.pop()
            if not curNode:
                continue

            counter += 1 
            if counter == k:
                return curNode.val
            curNode = curNode.right

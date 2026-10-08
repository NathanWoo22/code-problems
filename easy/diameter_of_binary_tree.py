# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        maxDiameter = 0
        def helper(root):
            nonlocal maxDiameter
            if not root:
                return 0

            lheight = helper(root.left)
            rheight = helper(root.right)
            maxDiameter = max(lheight + rheight, maxDiameter)
            return max(lheight, rheight) + 1

        helper(root)
        
        return maxDiameter
        

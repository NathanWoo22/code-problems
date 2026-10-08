# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balance = True
        def balanceHelper(root): 
            nonlocal balance
            if not root:
                return 0

            lheight = balanceHelper(root.left)
            rheight = balanceHelper(root.right)
            if abs(rheight - lheight) > 1:
                balance = False
            return max(lheight, rheight) + 1
        
        balanceHelper(root)
        return balance

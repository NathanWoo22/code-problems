# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def checkTree(node, upper, lower): 
            if node == None:
                return True
            
            if node.val >= upper or node.val <= lower: 
                return False

            # left node
            leftLower = lower
            leftUpper = node.val
            leftValid = checkTree(node.left, leftUpper, leftLower)

            # right node
            rightLower = node.val
            rightUpper = upper
            rightValid = checkTree(node.right, rightUpper, rightLower)

            return leftValid and rightValid
        
        return checkTree(root, float('inf'), float('-inf'))

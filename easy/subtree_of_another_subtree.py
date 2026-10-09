# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isSameTree(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2 or r1.val != r2.val:
                return False
            
            return isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)


        if root == None and subRoot == None:
            return True
        if root == None:
            return False
        
        sameTree = isSameTree(root, subRoot)
        if sameTree:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

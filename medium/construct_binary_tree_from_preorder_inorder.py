# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) == 0:
            return None

        node = TreeNode(preorder[0])
        nodeLoc = inorder.index(preorder[0])
        leftNode = self.buildTree(preorder[1: 1 + nodeLoc], inorder[0:nodeLoc])
        rightNode = self.buildTree(preorder[1 + nodeLoc:], inorder[nodeLoc + 1:])
        node.left = leftNode
        node.right = rightNode
        return node

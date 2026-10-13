# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxSum = -1000000
        
        def dfs(node):
            nonlocal maxSum
            if node == None:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            if leftMax > rightMax:
                curSum = node.val + leftMax
            else:
                curSum = node.val + rightMax
            maxSum = max(maxSum, node.val + rightMax + leftMax)
            return max(0, curSum) 
        
        dfs(root)
        return maxSum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        retList = []
        def dfs(node):
            nonlocal retList
            if node == None:
                retList.append("N")
                return
            
            retList.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(retList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        val = 0

        def dfs():
            nonlocal val, data
            if data[val] == "N":
                val = val + 1
                return None
            
            curNode = TreeNode(int(data[val]))
            val = val + 1
            curNode.left = dfs()
            curNode.right = dfs()
            return curNode
        
        return dfs()
            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

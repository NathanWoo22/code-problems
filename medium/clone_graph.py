"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        originalNode = node
        if node == None:
            return None
        newNodes = defaultdict(Node)
        visitedNodes = defaultdict(int)

        newNodes[node] = Node(node.val)
        stack = [node]
        visitedNodes[node] = 1
        while stack:
            node = stack.pop()

            for neighbor in node.neighbors:
                if visitedNodes[neighbor] == 0:
                    stack.append(neighbor)
                    visitedNodes[neighbor] = 1

                newNeighbor = newNodes[neighbor]
                newNeighbor.val = neighbor.val
                
                newNodes[node].neighbors.append(newNeighbor)
        
        return newNodes[originalNode]

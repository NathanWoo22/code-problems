"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            cur = head
            copyCur = None
            dummy = Node(0, copyCur, None)
            prev = dummy
            nodeMap = {None: None}
            counter = 0 
            while cur != None:
                copyCur = Node(cur.val, None, None)
                nodeMap[cur] = copyCur 
                prev.next = copyCur
                prev = copyCur
                cur = cur.next
                counter += 1
            
            cur = head
            copyCur = dummy.next
            counter = 0
            while cur != None:
                copyCur.random = nodeMap[cur.random]
                cur = cur.next
                copyCur = copyCur.next

            return dummy.next

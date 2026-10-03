# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        nodeList = []
        cur = head
        while cur != None:
            nodeList.append(cur)
            cur = cur.next

        l = 0
        r = len(nodeList) - 1
        iteration = 0
        while l != r: 
            if iteration % 2 == 0: 
                nodeList[l].next = nodeList[r]
                l += 1
            else:
                nodeList[r].next = nodeList[l]
                r -= 1
            iteration += 1
        nodeList[l].next = None
        return head

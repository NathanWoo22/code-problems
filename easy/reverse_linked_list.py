# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur = head
        prev = None
        newNode = None
        while cur != None:
            newNode = ListNode(cur.val, prev)
            prev = newNode 

            cur = cur.next

        return newNode

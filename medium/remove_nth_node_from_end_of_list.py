# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        front = head
        back = dummy
        for i in range(n):
            front = front.next
        
        while front != None:
            front = front.next
            back = back.next
        
        back.next = back.next.next
        
        return dummy.next

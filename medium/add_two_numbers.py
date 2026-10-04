# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add(self, l1: ListNode | None, l2: ListNode | None, carry: int) -> ListNode | None:
        if not l1 and not l2:
            if carry == 1:
                return ListNode(1, None)
            return None
        v1 = 0
        v2 = 0
        
        if l1:
            v1 = l1.val
            l1 = l1.next

        if l2:
            v2 = l2.val
            l2 = l2.next

        total = v1 + v2 + carry
        rem = 0
        if total > 9:
            total = total % 10
            rem = 1
        
        return ListNode(total, self.add(l1, l2, rem))

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        return self.add(l1, l2, 0) 

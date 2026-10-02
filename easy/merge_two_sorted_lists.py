
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        n1 = list1
        n2 = list2
        head = None 
        cur = None
        prev = None
        while n1 != None or n2 != None:
            if n1 == None:
                cur = n2
                n2 = None
            elif n2 == None:
                cur = n1
                n1 = None
            elif n1.val < n2.val:
                cur = ListNode(n1.val, None)
                n1 = n1.next
            else:
                cur = ListNode(n2.val, None)
                n2 = n2.next
            if head == None:
                head = cur
            if prev != None:
                prev.next = cur

            prev = cur 
            cur = cur.next
        return head

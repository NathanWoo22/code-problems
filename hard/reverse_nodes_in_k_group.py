# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        cur = head
        for i in range(k):
            if cur == None:
                return head
            cur = cur.next
        
        new_head = self.reverseList(head, k)
        head.next = self.reverseKGroup(cur, k)
        return new_head
    
    def reverseList(self, head, k):
        prev = None
        cur = head
        n = cur.next
        counter = 0
        while counter < k:
            cur.next = prev
            prev = cur
            cur = n
            if n == None:
                break
            n = n.next
            counter += 1
        return prev

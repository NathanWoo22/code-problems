# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vals = set()
        cur = head

        while cur:
            if cur in vals:
                return True
            vals.add(cur)
            cur = cur.next
        
        return False

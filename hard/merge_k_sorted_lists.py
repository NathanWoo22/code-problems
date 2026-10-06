# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            l1 = lists[0]
            l2 = lists[1]
        else:
            l1 = self.mergeKLists(lists[0:len(lists)//2])
            l2 = self.mergeKLists(lists[len(lists)//2:])
        
        newList = ListNode()
        cnew = newList
        c1 = l1
        c2 = l2
        while True: 
            if c1 == None:
                cnew.next = c2
                return newList.next
            elif c2 == None:
                cnew.next = c1
                return newList.next
            if c1.val < c2.val: 
                cnew.next = c1
                cnew = cnew.next
                c1 = c1.next
            else:
                cnew.next = c2
                cnew = cnew.next
                c2 = c2.next 
        return newList.next

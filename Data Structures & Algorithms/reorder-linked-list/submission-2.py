# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head
        lb = head
        ub = head
        fast = head

        while fast.next and fast.next.next:
            ub = ub.next
            fast = fast.next.next

        nxt = ub.next 
        ub.next = None
        ub = nxt
        prev = None
        while ub:
            nxt = ub.next
            ub.next = prev
            prev = ub 
            ub = nxt
        cur = prev
        ub = prev
        prevlb = lb
        prevub = ub
        cur = lb
        while ub:
            nxtlb = lb.next
            nxtub = ub.next
            lb.next = ub
            ub.next = nxtlb
            prevlb = lb
            prevub = ub
            lb = nxtlb
            ub = nxtub


        
            




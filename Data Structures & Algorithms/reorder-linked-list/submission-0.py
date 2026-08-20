# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lb = head
        ub = head
        fast = head
        prev = None
        if head is None:
            return head

        while fast is not None and fast.next is not None:
            prev = ub
            ub = ub.next
            fast = fast.next.next

        if prev is not None:
            prev.next = None
        
        prev = ub
        ub = ub.next
        prev.next = None
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
        while lb:
            print(str(lb.val) + ' ' + str(ub.val))
            nxtlb = lb.next
            nxtub = ub.next
            lb.next = ub
            ub.next = nxtlb
            prevlb = lb
            prevub = ub
            lb = nxtlb
            ub = nxtub
        if ub:
            prevub.next = ub


        
            




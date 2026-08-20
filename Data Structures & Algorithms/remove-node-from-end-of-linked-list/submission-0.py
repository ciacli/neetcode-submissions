# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        sz = 0
        cur = head
        while cur:
            sz += 1
            cur = cur.next
        index = 1
        cur = head
        prev = None
        while index < (sz - n + 1):
            prev = cur
            cur = cur.next
            index += 1
        if (sz - n + 1) == 1:
            return head.next
        prev.next = cur.next
        return head
        
        
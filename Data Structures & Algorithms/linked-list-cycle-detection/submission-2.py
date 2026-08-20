# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head.next
        slow = head
        while fast is not None and fast != slow:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
        if fast is None:
            return False
        return True

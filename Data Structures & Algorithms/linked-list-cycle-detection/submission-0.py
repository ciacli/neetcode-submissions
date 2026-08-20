# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur is not None and cur.val != 1001:
            cur.val = 1001
            cur = cur.next
        if cur is None:
            return False
        return True
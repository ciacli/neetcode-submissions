# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, cur):
        if cur.next is None:
            return cur

        head = self.rec(cur.next)
        cur.next.next = cur
        cur.next = None
        return head
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        cur = head
        if head is None:
            return head
        newHead = self.rec(cur)
        return newHead

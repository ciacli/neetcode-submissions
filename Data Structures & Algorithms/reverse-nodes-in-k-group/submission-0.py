# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(next = head)
        before, last = dummy, dummy
        first = ListNode()
        after = ListNode()

        def reverse(cur, prev, k):
            if k == 0:
                return
            reverse(cur.next, cur, k - 1)
            cur.next = prev
        
        while last:
            before = last
            cnt = k
            while cnt > 0 and last:
                last = last.next
                cnt -= 1
            if not last:
                break
            first = before.next
            after = last.next
            reverse(cur = first, prev = before, k = k)
            before.next = last
            first.next = after
            last = first

        return dummy.next



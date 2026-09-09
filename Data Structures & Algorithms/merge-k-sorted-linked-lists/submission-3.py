# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from itertools import count
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        h = []
        cnt = count()
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, next(cnt), l))
        dummy = ListNode()
        cur = dummy
        nodesLeft = True
        while h:
            nodesLeft = False
            mn = ListNode(val = 10001)
            index = 0
            val, _, node = heapq.heappop(h)
            if not node:
                break
            cur.next = node
            cur = node
            node = node.next
            if not node:
                continue
            val = node.val
            heapq.heappush(h, (val, next(cnt), node))
        return dummy.next
                

            
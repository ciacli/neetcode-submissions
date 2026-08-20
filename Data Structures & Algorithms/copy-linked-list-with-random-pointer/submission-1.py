"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        cur = head
        while cur is not None:
            d[cur] = Node(x = cur.val)
            cur = cur.next
        cur = head
        while cur is not None:
            node = d[cur]
            rnd = d[cur.random] if cur.random is not None else None
            nxt = d[cur.next] if cur.next is not None else None
            node.next = nxt
            node.random = rnd
            cur = cur.next
        return d[head] if head is not None else None
        
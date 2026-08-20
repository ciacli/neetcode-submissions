# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        it1 = list1
        it2 = list2
        head = None
        if list1 is None and list2 is None:
            return list1
        if list1 is None: 
            head = list2
            it2 = it2.next
        elif list2 is None:
            head = list1
            it1 = it1.next
        elif list1.val <= list2.val:
            head = list1
            it1 = it1.next
        else:
            head = list2
            it2 = it2.next

        cur = head

        while it1 is not None and it2 is not None:
            if it1.val <= it2.val:
                cur.next = it1
                it1 = it1.next
            else:
                cur.next = it2
                it2 = it2.next
            
            cur = cur.next
        if it1 is not None:
            cur.next = it1
        if it2 is not None:
            cur.next = it2
        return head
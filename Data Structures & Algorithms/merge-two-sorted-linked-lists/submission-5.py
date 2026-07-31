# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        head = None
        res = None

        while curr1 != None and curr2 != None:
            val1, val2 = curr1.val, curr2.val

            if val1 < val2:
                if not head:
                    head = curr1
                    res = head
                    curr1 = curr1.next
                    continue
                head.next = curr1
                head = head.next
                curr1 = curr1.next
            else:
                if not head:
                    head = curr2
                    res = head
                    curr2 = curr2.next
                    continue
                head.next = curr2
                head = head.next
                curr2 = curr2.next

        if curr1 != None:
            if head:
                head.next = curr1
            else:
                head = curr1
                res = head
        
        if curr2 != None:
            if head:
                head.next = curr2
            else:
                head = curr2
                res = head
        return res

        
        
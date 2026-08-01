# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 1

        while curr:
            curr = curr.next
            length += 1

        index = 1
        midpoint = head
        while index < (length // 2):
            midpoint = midpoint.next
            index += 1

        first = head
        second = midpoint.next
        midpoint.next = None

        prev = None
        while second.next:
            nbor = second.next
            second.next = prev
            prev = second
            second = nbor
        second.next = prev

        curr = first
        first = first.next

        while first and second:
            fn = first.next
            sn = second.next

            curr.next = second
            second = sn
            curr = curr.next
            curr.next = first
            first = fn
            curr = curr.next

        if second:
            curr.next = second
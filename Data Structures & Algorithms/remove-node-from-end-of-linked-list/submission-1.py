# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, length = head, 0
        index = 1

        while curr:
            curr = curr.next
            length += 1

        curr = head
        res = curr
        prev = None

        while index < length - n + 1:
            prev = curr
            curr = curr.next
            index += 1

        if not prev:
            return curr.next
        else:
            prev.next = curr.next
            curr.next = None
            return res


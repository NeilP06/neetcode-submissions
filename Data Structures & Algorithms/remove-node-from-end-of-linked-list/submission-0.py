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


        curr = ListNode()
        res = curr
        curr.next = head

        if length > 2:
            curr = curr.next

        while index < length - n:
            curr = curr.next
            index += 1

        val = curr.next.val
        curr.next = curr.next.next

        return res.next        


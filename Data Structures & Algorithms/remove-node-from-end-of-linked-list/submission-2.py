# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Variables needed to track intermediary states, O(1) space
        curr, length = head, 0
        index = 1

        # Count length of the list, O(n) work
        while curr:
            curr = curr.next
            length += 1

        # Variables needed to build final result, O(1) space
        curr = head
        res = curr
        prev = None

        # Iterate until we reach the length-n+1-th position, keeping track of
        # node previous to it, O(n) work
        while index < length - n + 1:
            prev = curr
            curr = curr.next
            index += 1

        # Cut the intended element from the linked list, where there are two
        # cases: (1) the intended element is the head (in that case, go to the
        # next), or (2) the intended element is in the middle or end (in this
        # case, directly cut the element using the prev and next pointers)
        if not prev:
            return curr.next
        else:
            prev.next = curr.next
            curr.next = None
            return res


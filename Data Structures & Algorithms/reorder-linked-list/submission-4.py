# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Variables needed to find midpoint state, O(1) space
        slow, fast = head, head.next

        # Use the slow and fast pointer method to find the midpoint of the 
        # list, O(n) work
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # A list with one node cannot have two halves, so return early if
        # this is the case
        if not head.next:
            return 

        # Split the list into two halves, with the first pointing to the first
        # half and the second pointing to the second half, O(1) space and work
        first = head
        second = slow.next
        slow.next = None

        # Reverse the second half of the list, O(n) work
        prev = None
        while second.next:
            nbor = second.next
            second.next = prev
            prev = second
            second = nbor
        second.next = prev

        # Pointers to track intermediary states for merging both halves 
        # together, O(1) space
        curr = first
        first = first.next

        # Merge both halves together in a weaving pattern, O(n) work
        while first and second:
            fn = first.next
            sn = second.next

            curr.next = second
            second = sn
            curr = curr.next
            curr.next = first
            first = fn
            curr = curr.next

        # Lastly, as the second half is always G.E.Q. to the first half, check
        # for excess elements, O(1) work
        if second:
            curr.next = second
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Variables needed to track intermediary states and build final result,
        # O(1) space
        curr1, curr2 = list1, list2
        head = ListNode()
        res = head

        # Loop over, at most, twice the longest linked list, O(n) work
        while curr1 and curr2:            
            # Case on values to build the list, O(1) work
            head.next = curr1 if curr1.val < curr2.val else curr2
            head = head.next

            # Move the active pointer, O(1) work
            if curr1.val < curr2.val:
                curr1 = curr1.next
            else:
                curr2 = curr2.next
    
        # Clear out any remaining nodes left (either the first or the second
        # has nodes if they're not the same length), O(1) work
        if not curr1 or not curr2:
            head.next = curr1 if curr1 else curr2

        return res.next
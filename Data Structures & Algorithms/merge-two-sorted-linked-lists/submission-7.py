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
        head = None
        res = None

        # Loop over, at most, twice the longest linked list, O(n) work
        while curr1 and curr2:
            # Extract values from pointers, O(1) work
            val1, val2 = curr1.val, curr2.val

            # Case on values and the head state to build the list, O(1) work
            if val1 < val2:
                # Case 1: the first pointer will go before the second pointer
                if not head:
                    head = curr1
                    res = head
                    curr1 = curr1.next
                    continue

                head.next = curr1
                head = head.next
                curr1 = curr1.next
            else:
                # Case 2: the second pointer will go before the first pointer
                if not head:
                    head = curr2
                    res = head
                    curr2 = curr2.next
                    continue

                head.next = curr2
                head = head.next
                curr2 = curr2.next

        # Clear out any remaining nodes left (either the first or the second
        # has nodes if they're not the same length), O(1) work
        if not curr1 or not curr2:
            if not head:
                head = curr1 if curr1 else curr2
                res = head
            else:
                head.next = curr1 if curr1 else curr2

        return res
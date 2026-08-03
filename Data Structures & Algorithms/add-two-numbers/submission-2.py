# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Variables needed to track intermediary states, O(1) space
        res = l1
        curr1, curr2 = l1, l2
        last = curr1
        carryover = False
        
        # While the two lists are synchronized, we add their values together, 
        # using a carryover variable to track at what places we need to carry 
        # over the one to, O(n) work
        while curr1 and curr2:
            # Calculate total, O(1) work
            total = curr1.val + curr2.val + (1 if carryover else 0)

            # Set value, O(1) work
            if total >= 10:
                carryover = True
                curr1.val = total - 10
            else:
                carryover = False
                curr1.val = total

            # Update last point, O(1) work
            if curr1.next:
                last = curr1.next

            curr1 = curr1.next
            curr2 = curr2.next

        # Check if curr1 still has remaining variables, so that we could add 
        # carryovers if needed, O(n) work
        while curr1:
            # Calculate total, O(1) work
            total = curr1.val + (1 if carryover else 0)

            # Set value, O(1) work
            if total >= 10:
                carryover = True
                curr1.val = total - 10
            else:
                carryover = False
                curr1.val = total
            
            # Update last pointer, O(1) work
            if curr1.next:
                last = curr1.next

            curr1 = curr1.next

        # Use a special if statement to set curr1 and the last pointer in the
        # correct place before iterating over the second list if needed, O(1)
        # work
        if curr2:
            curr1 = last
            curr1.next = curr2
            last = curr2

        # Likewise to the first list, check if there are any elements in the 
        # second list for carryovers, O(n) work
        while curr2:
            # Calculate total, O(1) work
            total = curr2.val + (1 if carryover else 0)

            # Set value, O(1) work
            if total >= 10:
                carryover = True
                curr2.val = total - 10
            else:
                carryover = False
                curr2.val = total
            
            # Update last pointer if needed, O(1) work
            if curr2.next:
                last = curr2.next

            curr2 = curr2.next          
        
        # Lastly, add an extra digit if there is a carryover not resolved, O(1)
        # work
        if carryover:
            curr1 = last
            end = ListNode(1, None)
            curr1.next = end

        return res
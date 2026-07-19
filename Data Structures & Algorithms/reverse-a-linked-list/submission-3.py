# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Return early if there are no nodes in the list
        if not head:
            return None

        # Variables used to track intermediary states, O(1) space
        temp = head
        prev = None

        # Loop through the linked list linearly, O(n) work
        while temp != None and temp.next != None:
            # Shift the temp pointer ahead of the prev pointer by one and 
            # destroy the first .next pointer, O(1) work
            if prev == None:
                prev = temp
                temp = temp.next
                prev.next = None
                continue
            # Else, shift all pointers by one after making temp's next point
            # to prev, O(1) work
            nbor = temp.next
            temp.next = prev
            prev = temp 
            temp = nbor

        # Lastly, before returning, shift the last .next pointer to the prev, 
        # O(1) work
        temp.next = prev
        head = temp
        
        return head
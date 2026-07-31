# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Variables needed to track intermediary states, O(1) work
        t = head
        h = t

        # Run the tortoise node slowly, O(n) work
        while t:
            # Determine the conditions for the hare node
            if h and h.next:
                # Set hare double the distance the tortoise travels, O(1) work
                t = t.next
                h = h.next.next

                # We reached a cycle if the tortoise and the hare reach the 
                # same node, which is not possible if the list was acyclic,
                # return True here
                if t == h:
                    return True
            else:
                # Hare node ran too fast and hit the end, return False
                return False
            
        # Tortoise node eventually reached the end of list, indicating acyclic
        # properties, return False
        return False
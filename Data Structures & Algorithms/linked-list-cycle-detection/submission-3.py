# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head
        h = t


        while t:
            if h and h.next:
                h = h.next.next

                if t == h:
                    return True
                # elif not h:
                #     return False

                t = t.next
            else:
                return False
            
        # Tortoise node eventually reached the end of list, indicating acyclic
        # properties, return true
        return False
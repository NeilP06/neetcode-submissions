"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Variables needed to track intermediary states, O(n) space
        curr, deep_head = head, Node(0)
        start = deep_head
        translation = dict()

        # Iterate linearly to build a skeleton of the deep copy list, where
        # the random pointers still point back to the original list, O(n) work
        while curr:
            # Build skeleton of deep copy list, O(n) total space, O(1) work per
            # iteration
            dc = Node(curr.val, None, curr.random)
            start.next = dc
            start = start.next

            # Save the translation from the old copy to the new copy for the
            # second pass, O(1) work
            translation[curr] = dc

            curr = curr.next

        # Flip back to the start to begin the second iteration, O(1) work
        curr = dh.next

        # Do a second iteration to set the random pointers to the correct deep
        # copy pointer, O(n) work
        while curr:
            if curr.random:
                curr.random = translation[curr.random]
            curr = curr.next

        # Ignore dummy start, return head of new deep copy list
        return deep_head.next
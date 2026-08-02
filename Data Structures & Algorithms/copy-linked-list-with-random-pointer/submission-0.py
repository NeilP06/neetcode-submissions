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
        curr = head

        dh = Node(0)
        start = dh

        sh = Node(0)
        start2 = sh

        while curr:
            dc = Node(curr.val, None, curr.random)

            sc = Node(curr.val, None, curr)

            start.next = dc
            start = start.next

            start2.next = sc
            start2 = start2.next

            n = curr.next
            curr.next = start
            curr = n


        curr = dh.next

        while curr:
            if curr.random:
                curr.random = curr.random.next
            curr = curr.next

        curr = sh.next

        while curr:
            curr.random.next = None
            curr = curr.next
        
        return dh.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        res = ListNode()
        tracker = res

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
        
        while h:
            (val, i, node) = heapq.heappop(h)

            tracker.next = node
            tracker = tracker.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
                    
        return res.next
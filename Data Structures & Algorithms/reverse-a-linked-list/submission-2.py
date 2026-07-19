# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        temp = head
        prev = None

        while temp != None and temp.next != None:
            if prev == None:
                prev = temp
                temp = temp.next
                prev.next = None
                continue

            nbor = temp.next
            temp.next = prev
            prev = temp 
            temp = nbor
            print(prev.val, temp.val)


        temp.next = prev
        head = temp
        return head
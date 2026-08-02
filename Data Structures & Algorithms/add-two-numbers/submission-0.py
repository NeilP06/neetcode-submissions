# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = l1
        curr1, curr2 = l1, l2
        l = curr1
        carryover = False

        while curr1 and curr2:
            total = curr1.val + curr2.val
            total = total + 1 if carryover else total

            if total >= 10:
                carryover = True
                curr1.val = total - 10
            else:
                carryover = False
                curr1.val = total

            if curr1.next:
                l = curr1.next

            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            total = curr1.val + (1 if carryover else 0)

            if total >= 10:
                carryover = True
                curr1.val = total - 10
            else:
                carryover = False
                curr1.val = total
            
            if curr1.next:
                l = curr1.next

            curr1 = curr1.next


        if curr2:
            curr1 = l
            curr1.next = curr2

        while curr2:
            total = curr2.val + (1 if carryover else 0)

            if total >= 10:
                carryover = True
                curr2.val = total - 10
            else:
                carryover = False
                curr2.val = total
            
            if curr2.next:
                l = curr2.next

            curr2 = curr2.next          
        
        if carryover:
            end = ListNode(1, None)
            l.next = end


        return res
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        retenue = 0
        l3 = ListNode(0)
        temp = l3
        
        while True:
            if l1 is not None and l2 is not None:
                r = retenue + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                r = retenue + l1.val
                l1 = l1.next
            elif l2 is not None:
                r = retenue + l2.val
                l2 = l2.next
            elif retenue != 0:
                r = retenue
            else:
                break
            
            retenue = r // 10
            r = r % 10
            
            temp.val = r
            
            if l1 is not None or l2 is not None or retenue != 0:
                temp.next = ListNode(0)
                temp = temp.next
        
        return l3
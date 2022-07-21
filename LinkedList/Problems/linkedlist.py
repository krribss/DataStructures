#19. Remove Nth Node From End of List
#Definition for singly-linked list.
 
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p0 = head
        p1 = head

        for _ in range(n):
            p1 = p1.next

        if not p1:
            return head.next

        while p1.next:
            p0 = p0.next
            p1 = p1.next

        p0.next = p0.next.next
        return head
       
  ###################################################################
  
  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        LP = dummy
        for i in range(left - 1):
            LP  = curr  #secured the head
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            tempnext = curr.next
            curr.next = prev
            prev = curr
            curr = tempnext   #now required linked list is reversed

        LP.next.next = curr
        LP.next = prev
        return dummy.next
        

        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        m = 0
        while curr  :
            m += 1
            curr = curr.next

        if n == m:
            return head.next
            
        index = 0
        curr = head
        while index < m - n - 1 :
            curr = curr.next
            index += 1
        
        curr.next = curr.next.next
        return head


        
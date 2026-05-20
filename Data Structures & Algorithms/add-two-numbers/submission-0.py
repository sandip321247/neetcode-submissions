# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_digit = ListNode(-1)
        current = sum_digit
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 and curr2 :
            
            new_node = ListNode(((curr1.val + curr2.val) + carry)%10)
            current.next = new_node
            carry = (curr1.val + curr2.val + carry) // 10
            curr1 = curr1.next
            curr2 = curr2.next
            current = current.next
        while curr1:
            new_node = ListNode((curr1.val + carry)%10)
            current.next = new_node
            carry = (curr1.val +carry) // 10
            curr1 = curr1.next
            current = current.next
        while curr2:
            new_node = ListNode((curr2.val + carry)%10)
            current.next = new_node
            carry = (curr2.val +carry) // 10
            curr2 = curr2.next
            current = current.next

        if carry:
            current.next = ListNode(carry)

        return sum_digit.next
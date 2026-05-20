# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        l1 = list1   #l1 is the pointer to the head of list1
        l2 = list2   #l2 is the pointer to the head of list2

        curr  = dummy   #here curr is the pointer to dummy
        

        while l1 and l2:
            if l1.val >= l2.val:
                curr.next = l2  #attaches the node that l1 is pointing to
                l2 = l2.next


            else:
                curr.next = l1
                l1 = l1.next
            
            curr = curr.next    #moves curr forward to that same node

        #for the remaining part 
        if l1:
            curr.next = l1

        else:
            curr.next = l2

        return dummy.next
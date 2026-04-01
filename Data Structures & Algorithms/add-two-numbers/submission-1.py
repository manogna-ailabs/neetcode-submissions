# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        prev = dummy
        carry = 0
        while l1 or l2:
            sum_digit = carry
            if l1:
                sum_digit += l1.val
                l1 = l1.next
            if l2:
                sum_digit += l2.val
                l2 = l2.next
            curr = ListNode(sum_digit % 10)
            prev.next = curr
            prev = curr
            carry = sum_digit//10

        if carry:
            prev.next = ListNode(carry) 

        return dummy.next 

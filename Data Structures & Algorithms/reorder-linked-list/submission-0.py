# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        rev_second_half = self.reverseList(mid)
        
        mid.next=None

        curr1 = head
        curr2 = rev_second_half

        while curr1 and curr2:
            temp1 = curr1.next
            if temp1:
                curr1.next = curr2
            temp2 = curr2.next
            if temp2:
                curr2.next = temp1
            curr1, curr2 = temp1, temp2

        




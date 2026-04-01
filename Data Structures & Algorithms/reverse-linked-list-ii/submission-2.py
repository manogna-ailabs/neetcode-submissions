# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        # prev = None
        # curr = head
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        curr = head
        prev = None
        i = 1
        while i<left:
            temp = curr
            curr = curr.next
            prev = temp
            i+=1

        pre_left_pointer = prev

        prev = None
        reverse_start = curr
        while i < right+1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i+=1
        reverse_end = prev

        if left > 1:
            pre_left_pointer.next = reverse_end
        reverse_start.next = temp

        if left == 1:
            return reverse_end
        else:
            return head

         
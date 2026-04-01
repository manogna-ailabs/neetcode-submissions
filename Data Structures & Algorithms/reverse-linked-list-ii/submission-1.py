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
        # print("pre-left", pre_left_pointer.val)
        prev = None
        reverse_start = curr
        # print("reverse from", curr.val)
        while i < right+1:
            # print(curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i+=1
        reverse_end = prev
        # print("reverse end", reverse_end.val)
        # print("right", temp.val)

        if left > 1:
            pre_left_pointer.next = reverse_end
        reverse_start.next = temp

        if left == 1:
            return reverse_end
        else:
            return head

         
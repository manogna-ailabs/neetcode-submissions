# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        curr1 = head
        curr2 = head

        while curr1.next and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr1 == curr2:
                return True
            elif not curr1 or not curr2:
                return False

        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a: int, b: int):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        mid = ListNode(val = self.gcd(head.val, head.next.val))

        mid.next = head.next
        head.next = mid
        self.insertGreatestCommonDivisors(mid.next)

        return head
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_idx_map = {}
        curr = head

        dummy = Node(0)
        prev = dummy
        new_idx_node = {}

        i = 0
        while curr:
            new_node = Node(curr.val)
            prev.next = new_node
            prev = new_node

            node_idx_map[curr] = i
            new_idx_node[i] = new_node

            i += 1
            curr = curr.next

        prev.next = None

        j = 0
        curr = head
        new_list = dummy.next
        for j in range(i):
            if curr.random == None:
                new_list.random = None
            else:
                random_idx = node_idx_map[curr.random]
                new_list.random = new_idx_node[random_idx]

            curr = curr.next
            new_list = new_list.next

        return dummy.next           


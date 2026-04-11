"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def dfs(node):
            if not node:
                return None
            if node in clone:
                return clone[node]

            root = Node(node.val)
            clone[node] = root
            if node.neighbors:
                for neigh in node.neighbors:
                    cloneneigh = dfs(neigh)
                    root.neighbors.append(cloneneigh)
            return root
        return dfs(node)
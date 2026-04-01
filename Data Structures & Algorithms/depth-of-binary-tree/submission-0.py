# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        maxDepth = 1
        while stack:
            curr, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if curr.left:
                stack.append((curr.left, 1+depth))
            if curr.right:
                stack.append((curr.right, 1+depth))
        return maxDepth




        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

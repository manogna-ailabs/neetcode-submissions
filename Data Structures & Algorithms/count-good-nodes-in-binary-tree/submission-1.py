# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodes(root, stack):
            out = 0
            if not root:
                return 0
            node = root
            while stack:
                node, max_val = stack.pop()
                if node.val >= max_val:
                    out += 1
                    max_val = node.val
                if node.left:
                    stack.append((node.left, max_val))
                if node.right:
                    stack.append((node.right, max_val))
            return out
        return 1 + goodNodes(root.left, [(root.left, root.val)]) + goodNodes(root.right, [(root.right, root.val)])


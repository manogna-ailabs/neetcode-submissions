# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if (node1 and not node2) or (node2 and not node1):
                return False
            elif node1.val != node2.val:
                return False
            else:
                stack.append([node1.left, node2.left])
                stack.append([node1.right, node2.right])
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                if curr.val == subRoot.val:
                    if self.isSameTree(curr, subRoot):
                        return True
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return False

        







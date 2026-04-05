# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # res = []
        last_visited = None
        curr = root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            top = stack[-1]
            if top.right and last_visited != top.right:
                curr = top.right
            else:
                # res.append(top.val)
                last_visited = stack.pop()
                if top.val == target and not top.left and not top.right:
                    if stack:
                        parent = stack[-1]
                        if parent.left == top:
                            parent.left = None
                        if parent.right == top:
                            parent.right = None 
                    else:
                        return None
        return root
        
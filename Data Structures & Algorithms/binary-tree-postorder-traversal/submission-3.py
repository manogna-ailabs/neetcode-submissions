# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # stack = [root]
        # visit = [False]
        # while stack:
        #     cur, v = stack.pop(), visit.pop()
        #     if cur:
        #         if v:
        #             res.append(cur.val)
        #         else:
        #             stack.append(cur)
        #             visit.append(True)
        #             stack.append(cur.right)
        #             visit.append(False)
        #             stack.append(cur.left)
        #             visit.append(False) 
        # return res

        # res = []
        # def postorder(root):
        #     if not root:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)
        # postorder(root)
        # return res

        res = []
        stack = []
        curr = root
        last_visited = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            top = stack[-1]
            if top.right and last_visited != top.right:
                curr = top.right
            else:
                res.append(top.val)
                last_visited = stack.pop()
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def levelOrderRec(root, level):
            if not root:
                return
            if len(self.res) <= level:
                self.res.append([])
            self.res[level].append(root.val)
            levelOrderRec(root.left, level+1)
            levelOrderRec(root.right, level+1)
            return
        levelOrderRec(root, 0)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        def dfs(root):
            if not root:
                return (0, 0)
            leftRob, leftSkip = dfs(root.left)
            rightRob, rightSkip = dfs(root.right)
            rob = root.val + leftSkip + rightSkip
            skip = max(leftRob, leftSkip) + max(rightRob, rightSkip)
            return (rob, skip)

        maxVal = max(dfs(root))
        return maxVal
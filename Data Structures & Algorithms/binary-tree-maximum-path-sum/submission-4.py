# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        maxSum = root.val
        def dfs(root):
            nonlocal maxSum 
            if not root:
                return 0
            if not root.left and not root.right: # leaf node
                currSum = root.val
                maxSum = max(maxSum, currSum)
                return max(currSum,0)
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            currSum = root.val + leftSum + rightSum
            maxSum = max(maxSum, currSum)
            print(root.val, leftSum, rightSum, currSum)
            return root.val + max(leftSum, rightSum)
        dfs(root)
        return maxSum

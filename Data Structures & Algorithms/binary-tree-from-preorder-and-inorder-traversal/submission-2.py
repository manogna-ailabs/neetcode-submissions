# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        nodeToIndex = {v: i for i, v in enumerate(inorder)}

        def buildsubTree(root_idx, l, r):
            if l == r:
                return None

            root = TreeNode(preorder[root_idx])
            nLeft = nodeToIndex[root.val] - l

            left_idx = root_idx+1
            root.left = buildsubTree(left_idx, l, nodeToIndex[root.val])
            right_idx = root_idx + nLeft + 1
            root.right = buildsubTree(right_idx , nodeToIndex[root.val]+1, r)
            return root
        
        root = buildsubTree(0, 0, len(preorder))
        
        return root
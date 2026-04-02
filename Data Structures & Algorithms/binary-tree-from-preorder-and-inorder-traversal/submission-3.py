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

            root = TreeNode(preorder[root_idx]) # get root node val subtree from preorder

            left_idx = root_idx+1               # index of left node in preorder
            rLeft = nodeToIndex[root.val]       # inorder range for left node: (l, rLeft)
            root.left = buildsubTree(left_idx, l, rLeft)

            nLeft = rLeft - l                    # number of nodes in left tree
            right_idx = root_idx + nLeft + 1     # index of right node in preorder
            root.right = buildsubTree(right_idx , rLeft+1, r)   # inorder range for right node: (rLeft+1, r)
            return root
        
        root = buildsubTree(0, 0, len(preorder)) # root idx in preorder=0; range for whole tree (0, len(tree))
        
        return root
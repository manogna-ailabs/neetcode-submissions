# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                elif curr.left.val < val < curr.val:
                    temp = curr.left
                    if temp.right and temp.right.val > val:
                        right = temp.right
                        temp.right = None
                    else:
                        right = None
                    curr.left = TreeNode(val, left=temp, right=right)
                    return root
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                elif curr.val < val < curr.right.val:
                    temp = curr.right
                    if temp.left and temp.left.val < val:
                        left = temp.left
                        temp.left = None
                    else:
                        left = None
                    curr.right = TreeNode(val, left=left, right=temp)
                    return root
                else:
                    curr = curr.right
        return root 

                 

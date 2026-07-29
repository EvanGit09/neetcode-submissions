# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ### recursively swap sub trees

        # if current sub tree root is empty then just return
        if not root:
            return root

        # save the inverted right
        tempRight = None
        if root.right:
            tempRight = self.invertTree(root.right)
        
        # set right child subtree to left child sub tree (if it exists - otherwise set to None)
        if root.left:
            root.right = self.invertTree(root.left)
        else:
            root.right = None

        # set left subtree to right subtree we saved earlier
        root.left = tempRight

        # return the binary tree - which is now inverted
        return root
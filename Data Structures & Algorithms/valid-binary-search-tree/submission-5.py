# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        left = self.validLeft(root, root.left)
        right = self.validRight(root, root.right)

        if not (left and right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def validLeft(self, root, subRoot):
        if subRoot is None:
            return True
        elif subRoot.val >= root.val:
            return False
        return self.validLeft(root, subRoot.left) and self.validLeft(root, subRoot.right)
    def validRight(self,root,subRoot): 
        if subRoot is None:
            return True
        elif subRoot.val <= root.val:
            return False
        return self.validRight(root, subRoot.left) and self.validRight(root, subRoot.right)
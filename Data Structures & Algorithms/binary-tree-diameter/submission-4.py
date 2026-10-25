# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = 0 
        def dfs(root): 
            nonlocal count
            if root is None:
                return 0 
            left = self.heightCount(root.left)
            right = self.heightCount(root.right)
            count = max(count, left + right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return count
    def heightCount(self,root):
        if root is None:
            return 0 
        return 1 + max(self.heightCount(root.left), self.heightCount(root.right))
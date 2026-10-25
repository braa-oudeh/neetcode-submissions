# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root): 
            if root is None:
                return True 
            left = self.countHeight(root.left)
            right = self.countHeight(root.right)

            if abs(right - left) > 1: 
                return False
            return dfs(root.left) and dfs(root.right)
        return dfs(root)
    def countHeight(self, root): 
        if root is None:
            return 0 
        return 1 + max(self.countHeight(root.left), self.countHeight(root.right))
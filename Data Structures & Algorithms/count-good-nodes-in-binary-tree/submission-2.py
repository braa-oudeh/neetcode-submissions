# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxSoFar): 
            if not root:
                return 0  
            good = 0 
            if root.val >= maxSoFar: 
                good = 1 
            maxSoFar = max(root.val, maxSoFar)
            return good + dfs(root.left,maxSoFar) + dfs(root.right, maxSoFar)
        
        return dfs(root,root.val)
        
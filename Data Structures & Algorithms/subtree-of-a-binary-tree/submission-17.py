# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,subRoot):
            if not root and subRoot:
                return False 
            if root.val == subRoot.val and self.isSameTree(root,subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot) 
    
    def isSameTree(self,p,q): 
        if not p and not q: 
            return True 
        if p and not q or q and not p: 
            return False 
        if p.val !=  q.val: 
            return False 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
    
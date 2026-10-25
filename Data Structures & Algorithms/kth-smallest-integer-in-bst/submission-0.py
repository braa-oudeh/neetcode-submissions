# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        new_list = (self.getAllElements(root))
        return new_list[k-1]
    def getAllElements(self,root: Optional[TreeNode]): 
        if root is None: 
            return []
        else:
            return self.getAllElements(root.left) + [root.val] + self.getAllElements(root.right)
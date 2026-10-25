# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]

        while q: 
            len_q = len(q)
            level = []

            for i in range(len(q)): 
                s = q.pop(0)
                if s: 
                    level.append(s.val)
                    q.append(s.left)
                    q.append(s.right)
            if level: 
                res.append(level)
        return res
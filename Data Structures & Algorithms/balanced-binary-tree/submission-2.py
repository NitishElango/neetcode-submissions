# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cond = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            else:
                l = dfs(root.left)
                r = dfs(root.right)
                if abs(r-l) > 1:
                    self.cond = False
                return 1 + max(l,r)
        if not root:
            return True
        else:
            dfs(root)
        return self.cond
            
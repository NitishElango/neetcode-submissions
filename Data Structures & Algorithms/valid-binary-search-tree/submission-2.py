# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        def dfs(root, b, t):
            if not root:
                return
            else:
                if root.val <= b or root.val >= t:
                    self.valid = False
                else:
                    dfs(root.left, b, root.val)
                    dfs(root.right, root.val, t)
        if not root:
            return True
        else:
            dfs(root, float("-inf"), float("inf"))
            return self.valid
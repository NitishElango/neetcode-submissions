# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(root):
            if not root:
                return 0
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                node = 1 + max(left, right)
                self.longest = max(self.longest, left + right)
                return node
        dfs(root)
        return self.longest
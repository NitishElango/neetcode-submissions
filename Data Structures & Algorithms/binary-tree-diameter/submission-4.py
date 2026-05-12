# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diamater = 0
        def maxDepth(root):
            if not root:
                return 0
            else:
                l = maxDepth(root.left)
                r = maxDepth(root.right)
                self.max_diamater = max(self.max_diamater, l + r)
                return 1 + max(l, r)
        maxDepth(root)
        return self.max_diamater
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxd = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = 0
        def maxDepth(root):
            if not root:
                return 0
            else:
                l, r = maxDepth(root.left), maxDepth(root.right)
                self.maxd = max(self.maxd, l+r)
                return 1 + max(l,r)
        if not root:
            return 0
        else:
            print(maxDepth(root))
            return self.maxd
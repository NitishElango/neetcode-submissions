# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True
        elif p.val != q.val:
            return False
        else:
            left, right = False, False
            if p.left and q.left:
                left = self.isSameTree(p.left, q.left)
            if p.right and q.right:
                right = self.isSameTree(p.right, q.right)
            if not p.left and not q.left:
                left = True
            if not p.right and not q.right:
                right = True
            if left and right:
                return True
            else:
                return False
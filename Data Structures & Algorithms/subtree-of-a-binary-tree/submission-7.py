# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(p,q):
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False
            else:
                l,r = same(p.left, q.left), same(p.right, q.right)
                return l and r

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        else:
            q = deque([root])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if same(node, subRoot):
                        return True
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return False
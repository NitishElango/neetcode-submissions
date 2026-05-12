# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            else:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def isSubroot(p, subRoot):
            if not p and not subRoot:
                return True
            if not p or not subRoot:
                return False
            if p.val != subRoot.val:
                return isSubroot(p.left, subRoot) or isSubroot(p.right, subRoot)
            if p.val == subRoot.val:
                if sameTree(p, subRoot):
                    return True
                else:
                    return isSubroot(p.left, subRoot) or isSubroot(p.right, subRoot)
        return isSubroot(root, subRoot)


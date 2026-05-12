# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(r, s):
            if not r and not s:
                return True
            elif not r or not s or r.val != s.val:
                return False
            else:
                return same(r.left, s.left) and same(r.right, s.right)

        q = deque([root])
        while q:
            r = q.popleft()
            if r.val == subRoot.val:
                if same(r, subRoot):
                    return True
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        q1, q2  = [p], [q]
        while q1 and q2:
            n = len(q1)
            for _ in range(n):
                node1, node2 = q1.pop(0), q2.pop(0)
                if node1.left:
                    if not node2.left:
                        return False
                    q1.append(node1.left)
                if node1.right:
                    if not node2.right:
                        return False
                    q1.append(node1.right)
                if node2.left:
                    if not node1.left:
                        return False
                    q2.append(node2.left)
                if node2.right:
                    if not node1.right:
                        return False
                    q2.append(node2.right)
                if node1.val != node2.val:
                    return False
        return True

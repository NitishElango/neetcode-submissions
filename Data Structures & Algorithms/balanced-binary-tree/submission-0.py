# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [1]
        def height(node):
            if not node:
                return 0
            if not node.right and not node.left:
                return 1
            else:
                left = height(node.left)
                right = height(node.right)
                if abs(left - right) > 1:
                    res[0] = -1
                return 1 + max(left, right)
        if not root:
            return True
        else:
            height(root)
        return res[0] == 1
            

            
       
        
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
        
        res1, res2 = [p.val],[q.val]
        q1,q2 = deque([p]), deque([q])

        while len(q1) > 0:
            for i in range(len(q1)):
                node = q1.popleft()
                if node.left:
                    q1.append(node.left)
                    res1.append(node.left.val)
                else:
                    res1.append(None)
                if node.right:
                    q1.append(node.right)
                    res1.append(node.right.val)
                else:
                    res1.append(None)

        while len(q2) > 0:
            for i in range(len(q2)):
                node = q2.popleft()
                if node.left:
                    q2.append(node.left)
                    res2.append(node.left.val)
                else:
                    res2.append(None)
                if node.right:
                    q2.append(node.right)
                    res2.append(node.right.val)
                else:
                    res2.append(None)
        return res1 == res2
                
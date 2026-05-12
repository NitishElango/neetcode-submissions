# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        stack = deque([root])
        seen = set()
        count = 0
        while len(stack) > 0:
            node = stack[-1]
            #print(node.val)
            if node.left and node.left not in seen:
                stack.append(node.left)
            else:
                count +=1
                if count == k:
                    return stack[-1].val
                seen.add(stack.pop())
                if node.right:
                    stack.append(node.right)
            for node in stack:
                print(node.val)
        


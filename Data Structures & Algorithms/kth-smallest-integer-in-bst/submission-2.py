# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        q = deque([root])
        heap = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                heapq.heappush(heap, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        for _ in range(k):
            pop = heapq.heappop(heap)
        return pop
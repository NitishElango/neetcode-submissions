"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = set()
        clones = dict()
        curr = head
        start = head
        if not head:
            return None
        while curr:
            new_node = Node(curr.val)
            clones[curr] = new_node
            curr = curr.next
        while head:
            if head.next:
                clones[head].next = clones[head.next]
            else:
                clones[head].next = None
            if head.random:
                clones[head].random = clones[head.random]
            else:
                clones[head].random = None
            head = head.next
        return clones[start]
        
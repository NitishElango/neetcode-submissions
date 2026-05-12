"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
arr  = [1,2]
arr2 = arr
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Visit every node of the graph and store a copy in a dictionary
            # key -> og node, val -> new node
        # Visit every node again:
            # rebuild the neihbhors but this time using the new node
        if not node:    
            return None
        q = deque([node])
        node_copy = dict()
        visited = set()
        while q:
            n = q.popleft()
            newNode = Node(n.val)
            node_copy[n] = newNode
            visited.add(n)
            for neighbhor in n.neighbors:
                if neighbhor not in visited:
                    q.append(neighbhor)
        
        visited = set()
        q2 = deque([node])
        visited.add(node)
        while q2:
            n = q2.popleft()
            for neighbor in n.neighbors:
                node_copy[n].neighbors.append(node_copy[neighbor])
                if neighbor not in visited:
                    q2.append(neighbor)
                    visited.add(neighbor)

        return node_copy[node]
                    
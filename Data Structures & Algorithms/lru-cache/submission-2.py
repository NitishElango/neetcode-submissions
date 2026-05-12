class Node():
    def __init__(self, val = 0, key = 0, prev = None, nex = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nex = nex

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.nex = self.right
        self.right.prev = self.left
        self.hashmap = dict()
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node(key)
            return self.hashmap[key].val
        else:
            return -1

    def move_node(self, key):
        prev_node, next_node = self.hashmap[key].prev, self.hashmap[key].nex
        prev_node.nex = next_node
        next_node.prev = prev_node
        temp = self.left.nex
        self.left.nex = self.hashmap[key]
        self.hashmap[key].prev = self.left
        self.hashmap[key].nex = temp
        temp.prev = self.hashmap[key]
    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            if len(self.hashmap) + 1 > self.capacity:
                #need to evict
                del self.hashmap[self.right.prev.key]
                self.right.prev.prev.nex = self.right
                self.right.prev = self.right.prev.prev
            self.hashmap[key] = Node(value, key, None, None)
             #node to move to front
            temp = self.left.nex
            self.left.nex = self.hashmap[key]
            self.hashmap[key].prev = self.left
            self.hashmap[key].nex = temp
            temp.prev = self.hashmap[key]

        else:
            self.hashmap[key].val = value
            self.move_node(key)

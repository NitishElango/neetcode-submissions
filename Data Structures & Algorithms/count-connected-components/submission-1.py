class UnionFind():
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.components = n
    def find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    def union(self,a,b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.rank[ra] >= self.rank[rb]:
                self.parent[rb] = ra
                self.rank[ra] +=1
            else:
                self.parent[ra] = rb
                self.rank[rb] +=1
            self.components-=1
    def get_components(self):
        return self.components
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        return uf.get_components()
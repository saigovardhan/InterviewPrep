"""
minimum spanning tree
disjoint set
union find
"""

class UnionFind:
    def __init__(self, edges) -> None:
        self.parent = [i for i in range(edges+1)]
        self.weight = [1 for i in range(edges+1)]
    

    def find_ultimate_parent(self,node):
        if node ==self.parent[node]:
            return node
        else:
            return self.find_ultimate_parent(self.parent[node])
        
    def findBySize(self,u, v):
        up = self.find_ultimate_parent(u)
        vp = self.find_ultimate_parent(v)

        if self.weight[up] < self.weight[vp]:
            self.parent[up] = vp
            self.weight[up] += self.weight[vp]
        else:
            self.parent[vp] = up
            self.weight[vp] += self.weight[up]
    
    def print(self):
        print(self.parent)
        print(self.weight)
    

def main():
    d = UnionFind(7)
    d.findBySize(1, 2)
    d.findBySize(2, 3)
    d.findBySize(4, 5)
    d.findBySize(6, 7)
    d.findBySize(5, 6)
    if d.find_ultimate_parent(3) == d.find_ultimate_parent(7):
        print("same")
    else:
        print("not same")
    d.findBySize(3, 7)
    if d.find_ultimate_parent(3) == d.find_ultimate_parent(7):
        print("same")
    else:
        print("not same")


main()
        

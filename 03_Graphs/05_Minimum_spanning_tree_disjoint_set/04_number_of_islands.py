"""
delete
"""
class DisjoinSet:
    def __init__(self, v) -> None:
        self.parent = [i for i in range(v+1)]
        self.size = [1 for _ in range(v+1)]
    def findUltimateParent(self, node):
        if self.parent[node]==node:
            return node
        else:
            return self.findUltimateParent(self.parent[node])
    def unionBySize(self, u, v):
        ulp_u = self.findUltimateParent(u)
        ulp_v = self.findUltimateParent(v)
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
    def print(self):
        print(self.size)
        print(self.parent)
    def getUnion(self):
        return [self.parent, self.size]
        
edges = [[0,1],[0,2],[0,3],[1,2],[2,3],[4,5],[5,6],[7,8]]
n =9
m = 8
n1 = 4
m1 = 3
edge1=[ [0,  1], [ 0, 2], [1, 2]]
def main():
    d = DisjoinSet(3)
    for edge in edge1:
        d.unionBySize(edge[0], edge[1]) 
    parent , size = d.getUnion()
    need_edges = 0
    for i,node in enumerate(parent):
        if parent[node]==i:
            need_edges+=1
    d.print()
    print(need_edges)
main()
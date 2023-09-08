"""
prims algorithms 

adjList = { {0, 1, 2}, {0, 2, 1}, {1, 2, 1}, {2, 3, 2}, {3, 4, 1}, {4, 2, 2}}
"""
from heapq import heappush, heappop

def prims_algorithm(edges):
    nodes = len(edges)
    adjList = [[] for i in range(len(edges))]
    seen = [0 for _ in range(nodes+1)]
    minHeap = []
    for parent, child, wt in edges:
        adjList[parent].append([wt, child])
    
    heappush(minHeap, [0, 0])
    sol = 0
    while minHeap:
        pwt, pnode = heappop(minHeap)
        if seen[pnode] ==1:continue
        seen[pnode] = 1
        sol+=pwt
        for wt,child in adjList[pnode]:
            heappush(minHeap,[wt, child])

    print(sol)

prims_algorithm([
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 1],
    [4, 2, 2]
])
            

        


    



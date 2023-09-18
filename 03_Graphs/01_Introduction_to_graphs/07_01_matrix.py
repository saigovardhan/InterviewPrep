"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from collections import deque
def zero_one_matrix(grid):
    r = len(grid)
    c = len(grid[0])
    visited = [[float("inf") for _ in range(c)] for _ in range(r)]
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    queue = deque()
    for i in range(r):
        for j in range(c):
            if grid[i][j] ==0:
                queue.append([i, j, 0])
                visited[i][j] =0
            
    
    while queue:
        pr, pc, dist = queue.popleft()

        for d in directions:
            nr = pr+d[0]
            nc = pc+d[1]
            if nr < r and nr >=0 and nc < c and nc >= 0:
                if grid[nr][nc] == 1 and dist+1 < visited[nr][nc]:
                    visited[nr][nc] = dist+1
                    queue.append([nr, nc, dist+1])

    print(visited)


zero_one_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
zero_one_matrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])


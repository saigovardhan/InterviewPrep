"""
130. Surrounded Regions
Solved
Medium
Topics
Companies
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""

"""
go through all the edges, add all "O" 's to queue
create visited array and initilize all values to "X"
while adding zeroes to queue, mark them as "O" in visited
now pop from queue, do a dfs on 4 directions
if grid[nr][nc] ==0 mark visited[nr][nc] = 0
return visited

"""
from collections import deque
def surrounded_region(grid):
    r = len(grid)
    c = len(grid[0])
    visited = [["X" for _ in range(c)] for _ in range(r)]
    directions =[[-1, 0], [0, -1], [0, 1], [1, 0]]

    
    for i in range(r):
        if grid[i][0] ==0:
            dfs(i, 0, grid, directions, visited)

        if grid[i][c-1] ==0:
            dfs(i, c-1, grid, directions, visited)
    for j in range(c):
        if grid[0][j] ==0:
            dfs(0, j, grid, directions, visited)
        
        if grid[r-1][j] ==0:
            dfs(r-1, j, grid, directions, visited)
        
    print(visited)
def dfs(i, j, grid, directions, visited):
    visited[i][j] = "O"
    for d in directions:
        nr = d[0]+i
        nc = d[1]+j
        if nr < len(grid) and nr >=0 and nc < len(grid[0]) and nc >=0:
            if grid[nr][nc] =="O" and visited[nr][nc] =="X":
                visited[nr][nc] = "O"
                dfs(nr, nc, grid, directions, visited)


surrounded_region([["X", "X", "X", "X"], ["X", "O", "O", "X"], [
                  "X", "X", "O", "X"], ["X", "O", "X", "X"]])



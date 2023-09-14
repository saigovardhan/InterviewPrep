"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

def number_of_provinces(grid):
    r = len(grid)
    c = len(grid[0])
    directions = [[-1, 0],[0, 1], [1, 0],[0, -1]]
    visited = [[0 for _ in range(c)] for _ in range(r)]
    provinces = 0
    for i in range(r):
        for j in range(c):
            if visited[i][j]==0 and grid[i][j] ==1:
                provinces+=1
                dfs(i, j, grid, visited, directions)
    print(provinces)

def dfs(i, j, grid, visited, directions):
    visited[i][j] = 1

    for d in directions:
        nr = i+d[0]
        nc = j+d[1]
        if nr < len(grid) and nr >=0 and nc < len(grid[0]) and nc >=0:
            if grid[nr][nc] ==1 and visited[nr][nc]==0:
                visited[nr][nc] = 1
                dfs(nr, nc, grid, visited, directions)
            
grid =[
    [1,1,0],
    [1,1,0],
    [0,0,1]
] 

number_of_provinces(grid)


"""
Number of Islands
Problem Statement: Given a grid of size NxM (N is the number of rows and M is the number of columns in the grid) consisting of ‘0’s (Water) and ‘1’s(Land). Find the number of islands.

Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Pre-req: Connected Components, Graph traversal techniques

Examples:

Example 1:

Input:


Output: 3

Explanation:


There are 3 islands as the different components are surrounded by water (i.e. 0), and there is no land connectivity in either of the 8 directions hence separating them into 3 islands.

Example 2:

Input:


"""
def number_of_islands(grid):
    r = len(grid)
    c = len(grid[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    islands = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1 and visited[i][j] ==0:
                dfs(i, j, grid, visited, directions)
                islands+=1
    print(islands)

def dfs(i, j, grid, visited, directions):
    visited[i][j] = 1
    for d in directions:
        nr = d[0]
        nc = d[1]
        if nr >=0 and nc >=0 and nr < len(grid) and nc < len(grid[0]):
            if visited[nr][nc] ==0 and grid[nr][nc] ==1:
                dfs(nr, nc, grid, visited, directions)
grid =[[1, 1, 0], [0, 0, 1], [0, 1, 0]]
number_of_islands(grid)

                


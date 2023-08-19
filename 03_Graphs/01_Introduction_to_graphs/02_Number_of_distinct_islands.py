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
grid =[]
number_of_islands(grid)

                


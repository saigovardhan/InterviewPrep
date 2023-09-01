def number_of_islands(grid):
    r = len(grid)
    c = len(grid[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    islands = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1 and visited[i][j] ==0:
                


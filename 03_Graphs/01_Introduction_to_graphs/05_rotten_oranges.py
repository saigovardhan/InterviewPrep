"""

Code

994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from collections import deque


def rotten_oranges(grid):
    r = len(grid)
    c = len(grid[0])

    visited = [[0 for _ in range(c)] for _ in range(r)]
    queue = deque()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                visited[i][j] = 2
                queue.append([i, j, 0])
            elif grid[i][j] == 1:
                visited[i][j] = 1
    print(visited)
    max_count = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    while queue:
        pr, pc, count = queue.popleft()
        for d in directions:
            nr = pr+d[0]
            nc = pc+d[1]
            if nr < r and nc < c and nr >= 0 and nc >= 0:
                if grid[nr][nc] == 1 and visited[nr][nc] == 1:
                    visited[nr][nc] = 2
                    queue.append([nr, nc, count+1])
                    max_count = max(max_count, count+1)
    print(max_count)


rotten_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]])

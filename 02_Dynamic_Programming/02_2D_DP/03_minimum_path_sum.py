"""
64. Minimum Path Sum
Medium
11.6K
150
Companies
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


def minimum_path_sum(grid):
    r = len(grid)-1
    c = len(grid[0])-1
    dp = [[float("inf") for _ in range(len(grid)+1)] for j in range(len(grid))]
    sol = memoization(r, c, grid, dp)
    print(sol)


def memoization(r, c, grid, dp):
    if r == 0 and c == 0:
        return grid[r][c]

    if r < 0 or c < 0:
        return float("inf")

    if dp[r][c] != float("inf"): return dp[r][c]

    up = grid[r][c] + memoization(r-1, c, grid, dp)
    left = grid[r][c] + memoization(r, c-1, grid, dp)

    dp[r][c]  = min(up, left)
    return dp[r][c]


minimum_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
minimum_path_sum([[1, 2, 3], [4, 5, 6]])

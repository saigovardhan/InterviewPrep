"""
62. Unique Paths
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""


def grid_unique_paths(m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m)]
    sol = memoization(m-1, n-1, dp)
    print(sol)

    sol = tabulation(m, n, dp)
    print(f"tabluation {sol}")


def memoization(m, n, dp):
    if m == 0 and n == 0:
        return 1
    if m < 0 or n < 0:
        return 0

    if dp[m][n] != 0:
        return dp[m][n]

    left = memoization(m, n-1, dp)
    up = memoization(m-1, n, dp)

    dp[m][n] = left+up
    return dp[m][n]


def tabulation(m, n, dp):
    dp[0][0] = 1

    for r in range(1, m):
        for c in range(1, n):
            right = dp[r][c-1]
            down = dp[r-1][c]
            dp[r][c] = down+right
    print(dp)


grid_unique_paths(3, 2)
grid_unique_paths(3, 7)

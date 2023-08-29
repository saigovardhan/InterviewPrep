"""
Problem Link: Ninja Training

A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day. Our task is to calculate the maximum number of merit points that the ninja can earn.

Example:

Sample Input 1:

3
1 2 5 
3 1 1
3 3 3
3
10 40 70
20 50 80
30 60 90
Sample Output 1:
11
210
Explanation Of Sample Input 1:
For the first test case,
One of the answers can be:
On the first day, Ninja will learn new moves and earn 5 merit points. 
On the second day, Ninja will do running and earn 3 merit points. 
On the third day, Ninja will do fighting and earn 3 merit points. 
The total merit point is 11 which is the maximum. 
Hence, the answer is 11.

For the second test case:
One of the answers can be:
On the first day, Ninja will learn new moves and earn 70 merit points. 
On the second day, Ninja will do fighting and earn 50 merit points. 
On the third day, Ninja will learn new moves and earn 90 merit points. 
The total merit point is 210 which is the maximum. 
Hence, the answer is 210.

Sample Input 2:

3
18 11 19
4 13 7
1 8 13

2
10 50 1
5 100 11
Sample Output 2:
45
110
"""


def ninja_training(n, grid):
    r = len(grid)-1
    pc = 3
    dp = [[0 for _ in range(4)] for _ in range(n)]
    sol = memoization(r, pc, grid, dp)
    print(f"memo {sol}")
    sol = tabulation(grid, dp)
    print(sol)


def memoization(r, pc, grid, dp):
    if r < 0:
        return 0
    if dp[r][pc] != 0:
        return dp[r][pc]
    max_c = 0
    for c in range(3):
        if c != pc:
            pick = grid[r][c] + memoization(r-1, c, grid, dp)
            max_c = max(max_c, pick)

    dp[r][pc] = max_c
    return dp[r][pc]


def tabulation(grid, dp):
    pc = 3
    previous_max =0
    for i in range(3):
        previous_max = max( grid[0][i] ,previous_max)
    dp[0][3] = previous_max
    max_c = 0
    for r in range(1,len(grid)):
        for pc in range(4):
            for c in range(3):
                if c != pc:
                    pick = grid[r][c] + dp[r-1][c]
                    max_c = max(max_c, pick)  
        dp[r][pc] = max_c
   
    return dp

            



ninja_training(
    2,

    [[10, 50, 1],
     [5, 100, 11]]
)

ninja_training(
    3,
    [[18, 11, 19],
     [4, 13, 7],
     [1, 8, 13]]
)
ninja_training(
    3,
    [
        [10, 40, 70],
        [20, 50, 80],
        [30, 60, 90],
    ]
)

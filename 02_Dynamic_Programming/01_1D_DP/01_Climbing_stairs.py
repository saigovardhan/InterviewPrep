def climbing_stairs(n):
    dp = [0 for _ in range(n+1)]
    # sol = memoization(n, n, dp)
    sol = tabulation(n, n, dp)
    print(sol)


def memoization(ind, n, dp):
    if ind < 0:
        return 0
    if ind <= 1:
        return 1
    if dp[ind] != 0:
        return dp[ind]
    one_step = memoization(ind-1, n, dp)
    two_step = memoization(ind-2, n, dp)

    return one_step+two_step


def tabulation(ind, n, dp):
    dp[0] = 1
    dp[1] = 1

    for ind in range(2, n+1):

        one_step = dp[ind-1]
        two_step = dp[ind-2]

        dp[ind] = one_step+two_step

    print(dp[n])


climbing_stairs(3)

def frog_jump_k_steps(nums, k):
    ind = len(nums)-1
    dp = [float("inf") for _ in range(ind+2)]
    # sol = memoization(ind, nums, k, dp)
    sol = tabulation(ind, nums,k , dp)

    print(sol)


def memoization(ind, nums, k, dp):
    if ind == 0:
        return 0

    if dp[ind] != float("inf"):
        return dp[ind]

    for i in range(1, k+1):
        if ind-i >= 0:
            take = memoization(ind-i, nums, k, dp)+abs(nums[ind]-nums[ind-i])
            dp[ind] = min(take, dp[ind])

    return dp[ind]

def tabulation(ind, nums, k, dp):
    dp[0] = 0
    for ind in range(1,len(nums)):
        for i in range(1, k+1):
            if ind-i>=0:
                take = dp[ind-i] + abs(nums[ind]-nums[ind-i])
                dp[ind] = min(take, dp[ind])
    print(dp)
    return dp[len(nums)-1]

frog_jump_k_steps([2, 5, 2], 1)

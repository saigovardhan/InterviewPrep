def frog_jump(nums):
    ind = len(nums)-1
    dp = [float("inf") for _ in range(ind+2)]
    # sol = memoization(ind, nums, dp)
    sol = tabulation(ind, nums, dp)
    print(sol)

def memoization(ind, nums, dp):
    if ind ==0: return 0

    if ind <0 : return float("inf")

    if dp[ind] !=float("inf") : return dp[ind]

    one_jump = memoization(ind-1, nums, dp) + abs(nums[ind]-nums[ind-1])

    two_jump = float("inf")
    if ind >1:
        two_jump = memoization(ind-2, nums, dp)+ abs(nums[ind]-nums[ind-2])

    dp[ind] = min(one_jump, two_jump)
    return dp[ind]

def tabulation(ind, nums, dp):

    dp[0] = 0

    for ind in range(1, len(nums)):
        one_jump = dp[ind-1] + abs(nums[ind]-nums[ind-1])
        two_jump = float("inf")
        if ind >1:
            two_jump = dp[ind-2] + abs(nums[ind]-nums[ind-2])
        dp[ind] = min(one_jump, two_jump)
    print(dp)
    return dp[len(nums)-1]
        






frog_jump([10 , 20, 30, 10])
frog_jump([10, 50, 10])

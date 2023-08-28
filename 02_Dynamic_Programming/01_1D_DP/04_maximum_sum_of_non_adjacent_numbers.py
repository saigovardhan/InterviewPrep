"""
arr = [1, 2, 4]
=> 1+4 = 5

arr = [1, 2, 10, 3]
=> 1+10 = 11 is maximum sum of non adjacent 

arr = [1, 2, 10, 3, 100]
=> 1+10+100 = 111 is maximum sum of non adjacent numbers
"""

def maximum_sum(nums):
    ind = len(nums)-1
    dp = [0 for _ in range(ind+2)]
    # sol = memoization(ind, nums, dp)
    sol = tabulation(ind, nums, dp)
    print(sol)

def memoization(ind, nums, dp):
    if ind ==0: return nums[ind]
    if ind <0 : return 0
    if dp[ind] != 0 : return dp[ind]
    pick = nums[ind] + memoization(ind-2, nums, dp)
    not_pick = 0+ memoization(ind-1, nums, dp)

    dp[ind] =  max(pick, not_pick)
    return dp[ind]

def tabulation(ind, nums, dp):
    dp[0] = nums[0]

    for ind in range(1, len(nums)):
        pick = nums[ind] + dp[ind-2]
        not_pick = 0+dp[ind-1]
        dp[ind] = max(pick, not_pick)
    print(dp)
    return dp[len(nums)-1]



maximum_sum([1, 2, 10, 3, 100])
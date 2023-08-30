"""
A subset/subsequence is a contiguous or non-contiguous part of an array, where elements appear in the same order as the original array.
For example, for the array: [2,3,1] , the subsequences will be [{2},{3},{1},{2,3},{2,1},{3,1},{2,3,1}} but {3,2} is not a subsequence because its elements are not in the same order as the original array.
"""


def subset_sum_target(nums, target):
    ind = len(nums)-1
    dp = [[None for _ in range(target+1)] for _ in range(len(nums))]
    # sol = memoization(ind, nums, target, dp)
    sol = tabulation(ind, nums, target, dp)
    print(sol)


def memoization(ind, nums, target, dp):
    if ind == 0:
        return target == nums[0]

    if dp[ind][target]!=None : return dp[ind][target]

    if nums[ind] <= target:
        if (memoization(ind-1, nums, target-nums[ind], dp)):
            dp[ind][target] =True
            return dp[ind][target]


    dp[ind][target] =  (memoization(ind-1, nums, target, dp))
    return dp[ind][target]

def tabulation(ind, nums, target, dp):
    for i in range(len(nums)):
        if nums[i] ==target:
            dp[0][i] = True
        
    for ind in range(1, len(nums)):
        for t in range(target):
            if (dp[ind-1][t-nums[ind]]):
                dp[ind][t] =True
            else:
                dp[ind][t] = dp[ind-1][t]
    
    print(dp)
    return dp[len(nums)-1][target-1]





subset_sum_target([1, 2, 3, 4], 4)
# subset_sum_target([1, 2, 3, 4], 5)

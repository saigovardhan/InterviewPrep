"""
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

"""


def partition_equal_subset(nums):
    total_sum = sum(nums)
    dp = [[None for _ in range(total_sum//2+1)] for _ in range(len(nums))]
    if total_sum % 2 != 0:
        print(False)
        return False
    sol = memoization(len(nums)-1, total_sum//2, nums, dp)
    print(dp)
    print(sol)


def memoization(ind, k, nums, dp):
    if k == 0:
        return True
    if ind == 0:
        return nums[ind] == k

    if ind < 0:
        return False
    if dp[ind][k] != None:
        return dp[ind][k]
    take = 0
    if nums[ind] <= k:
        take = memoization(ind-1, k-nums[ind], nums, dp)
        if take == True:
            dp[ind][k] = True
            return dp[ind][k]

    not_take = memoization(ind-1, k, nums, dp)
    dp[ind][k] = not_take
    return dp[ind][k]


partition_equal_subset([1, 5, 11, 5])

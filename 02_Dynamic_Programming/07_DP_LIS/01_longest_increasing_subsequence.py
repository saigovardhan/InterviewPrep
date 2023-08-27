"""
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing 
subsequence

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""
def longest_increasing_subsequence(nums):
    # dp = [[0 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
    sol = dfs(len(nums)-1, -1, nums)
    print(sol)

def dfs(ind, prev, nums):
    if ind<0:return 0

    pick = 0
    if prev ==-1 or nums[ind]<nums[prev]:
        pick = 1+ dfs(ind-1, ind, nums)

    not_pick = 0+ dfs(ind-1, prev, nums)

    return max(pick,not_pick)


longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])


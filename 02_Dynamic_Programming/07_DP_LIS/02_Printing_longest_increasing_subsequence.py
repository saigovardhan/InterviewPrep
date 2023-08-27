"""
same as 01_longest_increasing_subsequence
"""
def longest_increasing_subsequence(nums):
    dp = [[0 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]

    for ind in range(len(nums)-1, -1, -1):
        for prev in range(len(nums)-1, -2, -1):
            pick = 0
            if prev ==-1 or nums[ind]<nums[prev+1]:
                pick = 1+ dp[ind][ind]

            not_pick = 0+ dp[ind+1][prev+1]

            dp[ind][prev+1] = max(pick, not_pick)
    
    print(dp)
    print(dp[len(nums)-1][len(nums)-1])


longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])






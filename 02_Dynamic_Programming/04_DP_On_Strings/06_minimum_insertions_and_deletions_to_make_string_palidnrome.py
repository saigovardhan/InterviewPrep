"""
583. Delete Operation for Two Strings
Medium
5.4K
78
Companies
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""


def deletions_insertions_for_palindrome(s1, s2):
    dp = [[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    count = 0
    sol = tabulation(s1, s2, dp, count)
    l1 = len(s1)
    l2 = len(s2)
    print((l1-sol)+(l2-sol))


def tabulation(s1, s2, dp, count):
    for i in range(len(s1)):
        dp[i][0] = 0

    for j in range(len(s2)):
        dp[0][j] = 0

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                count = max(count, dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return count


deletions_insertions_for_palindrome("sea", "eat")

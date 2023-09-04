""" 
516. Longest Palindromic Subsequence
Medium
8.9K
314
Companies
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


def longest_palindromic_subsequence(s):
    p = s[len(s)::-1]
    dp = [[-1 for _ in range(len(s)+1)] for _ in range(len(p)+1)]
    count = 0
    sol = tabulation(s, p,count, dp)
    print(dp)
    print(sol)

def tabulation(s, p,count ,dp):
    for i in range(len(s)+1):
        dp[i][0] = 0
    for j in range(len(p)+1):
        dp[0][j] = 0
    
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if s[i-1] == p[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                count = max(dp[i][j], count)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return count


longest_palindromic_subsequence("cbbd")

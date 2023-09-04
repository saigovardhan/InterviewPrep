"""

1143.print Longest Common Subsequence

Given two strings text1 and text2, return the longest common subsequence. If there is no common subsequence, return "".

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: "ace"
Explanation: The longest common subsequence is "ace" .
Example 2:

Input: text1 = "abc", text2 = "abc"
Output:"abc"
Explanation: The longest common subsequence is "abc" .
Example 3:

Input: text1 = "abc", text2 = "def"
Output: ""
Explanation: There is no such common subsequence, so the result is "".

"""

def print_longest_common_subsequence(s1, s2):
    dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = len(s1),len(s2)
    sol = ""
    while i > 0 and j > 0:
        if s1[i-1]==s2[j-1]:
            sol+=s1[i-1]
            i-=1
            j-=1
        elif s1[i-1]>s2[j-1]:
            i-=1
        elif s1[i-1]<s2[j-1]:
            j-=1
    print("solution -> " + sol)

print_longest_common_subsequence("abc", "sai")


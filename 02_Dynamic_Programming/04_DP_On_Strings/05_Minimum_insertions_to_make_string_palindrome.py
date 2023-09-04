"""
1312. Minimum Insertion Steps to Make a String Palindrome
Hard
4.6K
60
Companies
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".



"""


def minimum_insertions_to_make_string_palindrome(s):
    p = s[len(s)::-1]
    dp = [[-1 for _ in range(len(s)+1)] for _ in range(len(p)+1)]
    count = 0
    sol = tabulation(s, p, dp, count)

    print(len(s)-sol)


def tabulation(s, p, dp, count):
    for i in range(len(s)+1):
        dp[0][i] = 0
        dp[i][0] = 0

    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if s[i-1] == p[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                count = max(count, dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return count

minimum_insertions_to_make_string_palindrome("mbadm")
minimum_insertions_to_make_string_palindrome("leetcode")

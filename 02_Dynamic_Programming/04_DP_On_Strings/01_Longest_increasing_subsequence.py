"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

def longest_increast_increasing_subsequence(s1, s2):
    i = len(s1)-1
    j = len(s2)-1

    sol = memoization(i, j, s1 , s2)
    print(sol)

def memoization(i,j, s1, s2):
    if i< 0 or j < 0 : return 0
    # if i==0 and j ==0: return 1 if s1[i] ==s2[j] else 0

    pick = 0
    if s1[i] == s2[j]:
        pick =1+ memoization(i-1, j-1, s1, s2)
        return pick
    
    not_pick =0+ max(
        memoization(i-1, j, s1, s2),
        memoization(i, j-1, s1, s2)
    )

    return not_pick

longest_increast_increasing_subsequence("abc","aef")
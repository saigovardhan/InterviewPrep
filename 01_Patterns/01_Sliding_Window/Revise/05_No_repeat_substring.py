"""
No-repeat Substring (hard)
We'll cover the following
Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""

def No_repeat_substring(s):
    start, end = 0, 0
    seen = {}
    res = 0

    for end in range(len(s)):

        if s[end] in seen:
            start = max(start, seen[s[end]]+1)
        
        seen[s[end]] = end

        res = max(res, end-start+1)



No_repeat_substring("aabccbb")
# No_repeat_substring("abbbb")
# No_repeat_substring("abccde")
        
        
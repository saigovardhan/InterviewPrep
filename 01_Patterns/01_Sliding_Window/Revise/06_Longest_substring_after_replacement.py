"""
Longest Substring with Same Letters after Replacement (hard)
We'll cover the following
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

"""

def longest_substring_after_replacement(s, k):
    start, end, max_repeated = 0, 0, 0
    res = 0
    seen ={}
    for end in range(len(s)):
        if s[end] not in seen:
            seen[s[end]] = 0
        seen[s[end]]+=1

        max_repeated = max(max_repeated, seen[s[end]])

        if end-start+1-max_repeated >k:
            seen[s[start]]-=1
            if seen[s[start]] ==0:
                del(seen[s[start]])
            start+=1

        res = max(res, end-start+1)
    print(res)



longest_substring_after_replacement("aabccbb", k=2)
longest_substring_after_replacement("abbcb", k=1)
longest_substring_after_replacement("abccde", 1)

"""
Time complexity : o(n)
Space complexity:o(1) -->since o(26) for hashmap
"""
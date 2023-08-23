"""
Smallest Window containing Substring (hard) #
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""
from math import inf
def smallest_window_containing_substring(s, p):
    start, end, seen, matched = 0, 0, {}, 0
    res = float(inf)
    sol = ""
    for c in p:
        if c not in seen:
            seen[c] = 0
        seen[c] +=1
    
    for end in range(len(s)):
        if s[end] in seen:
            seen[s[end]] -=1
            if seen[s[end]] ==0:
                matched+=1

            
        while matched == len(p):
            if(res > (end-start+1)):
                res = end-start+1
                sol = s[start:end+1]
            if s[start] in seen:
                if seen[s[start]] ==0:
                    matched-=1
                seen[s[start]] +=1
            start+=1
        
    print(sol)


smallest_window_containing_substring("aabdec", "abc")
smallest_window_containing_substring("abdabca", "abc")
smallest_window_containing_substring("adcad", "abc")

                

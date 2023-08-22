"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

def longest_sub_string_with_k_distinct_characters(s, k):
    start , end = 0, 0
    sub_string  = 0
    seen = {}

    while end < len(s):
        if s[end] not in seen:
            seen[s[end]] = 0
        seen[s[end]] +=1

        while len(seen) >k:
            seen[s[start]] -=1
            if seen[s[start]]<=0:
                del(seen[s[start]])
            start+=1
        
        sub_string = max(sub_string, (end-start+1))

        end+=1
    
    print(sub_string)
    

longest_sub_string_with_k_distinct_characters("araaci", 2)
longest_sub_string_with_k_distinct_characters("araaci", 1)
longest_sub_string_with_k_distinct_characters("cbbebi", 3)
    



    



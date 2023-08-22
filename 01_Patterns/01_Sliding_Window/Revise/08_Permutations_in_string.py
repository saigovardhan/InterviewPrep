"""
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have 
n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.

"""


def permutations_in_string(s, p):
    start, end , seen , res, matched = 0, 0, {}, 0 , 0
    for c in p:
        if c not in seen:
            seen[c] = 0
        seen[c]+=1
    
    for end in range(len(s)):
        if s[end] in seen:
            seen[s[end]] -=1 
            if seen[s[end]] ==0:
                matched+=1
        
        if matched == len(p):return True

        if end>=len(p)-1:
            if s[start] in seen:
                if seen[s[start]] ==0:
                    matched-=1
                seen[s[start]]+=1
            start+=1
        
    return False


print(permutations_in_string("oidbcaf", "abc"))
print(permutations_in_string("odicf", "dc"))
                

    
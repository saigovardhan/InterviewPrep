"""
String Anagrams (hard) #
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""

def string_anagrams(s, p):
    start, end, seen = 0, 0, {}
    for c in p:
        if c not in seen:
            seen[c] = 0
        seen[c] +=1

    matched , res = 0, []


    for end in range(len(s)):
        if s[end] in seen:
            seen[s[end]] -=1
            if seen[s[end]] ==0:
                matched+=1

        if matched ==len(p):
            res.append(start) 


        if end>=len(p)-1:
            if s[start] in seen:
                if seen[s[start]] ==0:
                    matched-=1
                seen[s[start]] +=1
            start+=1

    print(res)
string_anagrams("ppqp", "pq")
string_anagrams("abbcabc", "abc")

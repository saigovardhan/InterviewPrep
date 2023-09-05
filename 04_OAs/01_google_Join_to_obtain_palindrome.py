"""
Given an array of X strings in which each string consists of two lowercase English letters, join as many strings together as possible in order to obtain a palindrome.

Input: arr = ["ck", "kc", "ho", "kc", "gg"]
Output: 4

explanation being that the longest palindrome are "ckkc" and "kcck" which both have lengths of 4.
"""
from collections import defaultdict


def longestPalindrome(words: list[str]) -> int:
    seen = defaultdict(int)
    unpaired =0
    ans = 0
    START, END = 0, 1
    for word in words:
        if word[START] == word[END]:
            if seen[word]>0:
                unpaired-=1
                ans+=4
                seen[word]-=1
            else:
                seen[word]+=1
                unpaired+=1
        else:
            if seen[word[::-1]] >0:
                ans+=4
                seen[word[::-1]]-=1
            else:
                seen[word]+=1
    if unpaired >0:
        ans+=2
    print(ans)


longestPalindrome(["lc", "cl", "gg"])

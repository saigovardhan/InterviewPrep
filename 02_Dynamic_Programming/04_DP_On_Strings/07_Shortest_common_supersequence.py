"""
1092. Shortest Common Supersequence
Hard
4.4K
63
Companies
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"


find  longest increasing subsequence-> then print the subsequence -> while printing
if s1[i] == s2[j]:
    res + = s1[i]
    i-=1
    j-=1
elif dp[i-1][j]>dp[i][j-1]:
    res+=s1[i]
    i-=1
else:
    res+=s2[j]
    j-=1

"""

prime = int(1e9+7)


def countUtil(s1, s2, ind1, ind2, dp):
    if ind2 < 0:
        return 1
    if ind1 < 0:
        return 0

    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]

    if s1[ind1] == s2[ind2]:
        leaveOne = countUtil(s1, s2, ind1-1, ind2-1, dp)
        stay = countUtil(s1, s2, ind1-1, ind2, dp)

        dp[ind1][ind2] = (leaveOne + stay) % prime
        return dp[ind1][ind2]
    else:
        dp[ind1][ind2] = countUtil(s1, s2, ind1-1, ind2, dp)
        return dp[ind1][ind2]


def subsequenceCounting(t, s, lt, ls):
    dp = [[-1 for j in range(ls)] for i in range(lt)]
    return countUtil(t, s, lt-1, ls-1, dp)


def main():
    s1 = "babgbag"
    s2 = "bag"

    print("The Count of Distinct Subsequences is",
          subsequenceCounting(s1, s2, len(s1), len(s2)))


if __name__ == "__main__":
    main()

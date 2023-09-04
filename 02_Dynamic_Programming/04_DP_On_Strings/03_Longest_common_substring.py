def longest_common_substring(s1, s2):
    i, j = len(s1), len(s2)
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    sol = tabulation( s1, s2, 0, dp)
    print(dp)
    print(sol)

def tabulation(s1, s2, count, dp):
    sol = ""
    count = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                count = max(dp[i][j], count)
                sol+=s1[i-1]
            else:
                dp[i][j] = 0
    
    return count



longest_common_substring("abcdfhijkltuh", "abceghijkluyt")

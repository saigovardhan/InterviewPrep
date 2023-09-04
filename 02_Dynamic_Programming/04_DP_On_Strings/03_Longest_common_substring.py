def longest_common_substring(s1, s2):
    i, j = len(s1), len(s2)
    sol = memoization(i, j, s1, s2, 0)
    print(sol)


def memoization(i, j, s1, s2, count):
    if i == 0 or j == 0:
        return count

    if i < 0 or j < 0:
        return 0

    if s1[i-1] == s2[j-1]:
        return memoization(i-1, j-1, s1, s2, count+1)

    else:
        top = memoization(i-1, j, s1, s2, 0)
        left = memoization(i, j-1, s1, s2, 0)
        return max(count, max(left, top))


longest_common_substring("abceghijk", "abcdghija")

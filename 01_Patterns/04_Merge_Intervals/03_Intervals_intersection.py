# """
# Intervals Intersection(medium)
# We'll cover the following
# Problem Statement
# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1 = [[1, 3], [5, 6], [7, 9]], arr2 = [[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:

# Input: arr1 = [[1, 3], [5, 7], [9, 12]], arr2 = [[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

# interval_insertion(arr1 = [[1, 3], [5, 6], [7, 9]], arr2 = [[2, 3], [5, 7]])

# """
# from heapq import heappush, heappop

# def interval_insertion(arr1, arr2):
#     arr1.sort(key = lambda x: x[0])
#     arr2.sort(key = lambda x:x[0])

#     i =0
#     j =0

#     while i < len(arr1) or j < len(arr2):
#         #a overlaps b
#         if arr1[i][0] >= arr2[j][0] and arr1[i][1] <= arr2[j][1]:

#         #b overlaps a

#         if any of above is true:
#             resule.append(min(starts), max(ends))
        
#         if arr1[i][1] <arr2[j][1]:
#             i+=1
#         else:
#             j+=1
#     return result





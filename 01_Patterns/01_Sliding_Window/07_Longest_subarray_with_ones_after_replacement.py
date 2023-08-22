"""
Longest Subarray with Ones after Replacement (hard)
We'll cover the following
Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

def longest_subarray_with_ones_after_replacement(arr, k):
    start, end = 0, 0
    
    res = 0
    for end in range(len(arr)):
        if arr[end] ==0:
            k-=1
        
        while k < 0:
            if arr[start] ==0:
                k+=1
            start+=1
        
        res = max(res, end-start+1)
    
    print(res)


longest_subarray_with_ones_after_replacement(
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2)

longest_subarray_with_ones_after_replacement(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3)
            

            


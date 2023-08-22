"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""
from math import inf

def smallest_sub_array_with_given_sum(nums, s):
    start , end  = 0, 0
    smallest = float(inf)
    target = 0
    while end <len(nums):
        target+=nums[end]

        while target >=s:
            smallest = min(smallest, end-start+1)
            target-=nums[start]
            start+=1
        end+=1
    
    print(smallest)

smallest_sub_array_with_given_sum([2, 1, 5, 2, 3, 2], 7)
smallest_sub_array_with_given_sum([2, 1, 5, 2, 8], 7)

            


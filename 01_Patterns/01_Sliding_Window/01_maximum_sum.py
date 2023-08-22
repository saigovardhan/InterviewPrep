"""
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
def maximum_sum(nums, k):
    start, end = 0 , 0
    max_sum, temp_sum = 0, 0
    seen = {}

    while end < len(nums)-1:
        if nums[end] not in seen:
            seen[nums[end]] =0
        seen[nums[end]] +=1

        temp_sum+=nums[end]
        if end >=k-1:
            max_sum = max(max_sum, temp_sum)
            temp_sum-=nums[start]
            start+=1
        end+=1
    print(seen)
    del(seen[nums[0]])
    print(seen)
        
    print(max_sum)

maximum_sum([2, 1, 5, 1, 3, 2], 3)
maximum_sum([2, 3, 4, 1, 5], k=2)

        




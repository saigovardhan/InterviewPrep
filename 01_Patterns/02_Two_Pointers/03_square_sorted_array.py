"""
Squaring a Sorted Array (easy)
We'll cover the following
Problem Statement #
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""
from collections import deque
def squaring_sorted_array(nums):
    p1, p2 = 0, len(nums)-1
    sol = deque()
    while p1 <= p2:
        p1_sqr = nums[p1]*nums[p1]
        p2_sqr = nums[p2]*nums[p2]

        if p1_sqr>=p2_sqr:
            sol.appendleft(p1_sqr)
            p1+=1
        else:
            sol.appendleft(p2_sqr)
            p2-=1
    
    print(sol)

squaring_sorted_array([-2, -1, 0, 2, 3])

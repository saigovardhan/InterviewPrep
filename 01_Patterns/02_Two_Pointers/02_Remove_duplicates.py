"""
Remove Duplicates (easy)

Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

def remove_duplicates(nums):
    curr = 0
    next = 1

    for curr in range(len(nums)):
        if curr >=1:
            if nums[curr] != nums[curr-1]:
                nums[curr], nums[next] =  nums[next], nums[curr]
                next+=1

    print(nums)

remove_duplicates([2, 3, 3, 3, 6, 9, 9])
remove_duplicates([2, 2, 2, 11])



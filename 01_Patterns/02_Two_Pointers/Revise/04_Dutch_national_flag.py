"""
Dutch National Flag Problem (medium)

Problem Statement #
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""

def dutch_national_flag(nums):
    end = 0
    zerosPosition = 0
    twosPosition = len(nums)-1
    while end<=twosPosition:
        if nums[end] == 0:
            nums[end], nums[zerosPosition] = nums[zerosPosition], nums[end]
            zerosPosition+=1
            end+=1
        elif nums[end] ==1:
            end+=1
        else:
            nums[end], nums[twosPosition] = nums[twosPosition], nums[end]
            twosPosition-=1


    print(nums)
dutch_national_flag([1, 0, 2, 1, 0])



